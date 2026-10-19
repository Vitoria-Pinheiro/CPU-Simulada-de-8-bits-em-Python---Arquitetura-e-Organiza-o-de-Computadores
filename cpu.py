
from ula import ula, limitar_8bits


class CPU:

    def __init__(self):
        self.registradores = {
            "R0": 0,
            "R1": 0,
            "R2": 0,
            "R3": 0
        }

        # 16 posições de memória
        self.memoria = [0] * 16

        # Program Counter
        self.pc = 0

        # Estado da CPU
        self.halted = False

    def executar_instrucao(self, instrucao):

        # Tratamento para posições de memória vazias ou zeradas
        if not instrucao or instrucao == 0:
            self.pc += 1
            return

        partes = instrucao.replace(",", "").split()
        operacao = partes[0]

        # ==============================================
        # LOAD — IMPLEMENTADO
        # ==============================================
        # LOAD R0, 5
        # R0 <- 5
        if operacao == "LOAD":
            registrador = partes[1]
            valor = int(partes[2])

            self.registradores[registrador] = limitar_8bits(valor)
            self.pc += 1

        # ==============================================
        # STORE — IMPLEMENTADO
        # ==============================================
        # STORE R0, 15
        # MEM[15] <- R0
        elif operacao == "STORE":
            registrador = partes[1]
            endereco = int(partes[2])

            if endereco < 0 or endereco >= len(self.memoria):
                raise ValueError("Endereço de memória inválido")

            self.memoria[endereco] = self.registradores[registrador]
            self.pc += 1

        # ==============================================
        # ADD, SUB, AND, OR, XOR — IMPLEMENTADOS VIA ULA
        # ==============================================
        # Exemplo: ADD R0, R1 -> R0 <- R0 + R1
        elif operacao in ["ADD", "SUB", "AND", "OR", "XOR"]:
            reg_dest = partes[1]
            reg_src = partes[2]

            val_a = self.registradores[reg_dest]
            val_b = self.registradores[reg_src]

            # Chama a função ula importada
            resultado = ula(operacao, val_a, val_b)

            self.registradores[reg_dest] = resultado
            self.pc += 1

        # ==============================================
        # JMP — IMPLEMENTADO
        # ==============================================
        # JMP 8
        # PC <- 8
        elif operacao == "JMP":
            endereco = int(partes[1])

            if endereco < 0 or endereco >= len(self.memoria):
                raise ValueError("Endereço de salto inválido")

            self.pc = endereco

        # ==============================================
        # HALT — IMPLEMENTADO
        # ==============================================
        elif operacao == "HALT":
            self.halted = True

        else:
            raise ValueError(f"Instrução desconhecida: {operacao}")

    def ciclo(self):

        if self.halted:
            return

        # ==============================================
        # FETCH
        # ==============================================
        instrucao = self.memoria[self.pc]

        print()
        print("--------------------------------")
        print("FETCH")
        print("PC:", self.pc)
        print("Instrução:", instrucao)

        # ==============================================
        # DECODE + EXECUTE
        # ==============================================
        print("DECODE + EXECUTE")

        self.executar_instrucao(instrucao)

        # ==============================================
        # ESTADO
        # ==============================================
        self.mostrar_estado()

    def executar(self, max_ciclos=100):

        ciclos = 0

        while not self.halted:

            if ciclos >= max_ciclos:
                raise RuntimeError(
                    "Número máximo de ciclos atingido. "
                    "Verifique se existe um loop infinito."
                )

            self.ciclo()
            ciclos += 1

    def mostrar_estado(self):

        print("Registradores:")

        for nome, valor in self.registradores.items():
            print(f"  {nome} = {valor:02X} ({valor})")