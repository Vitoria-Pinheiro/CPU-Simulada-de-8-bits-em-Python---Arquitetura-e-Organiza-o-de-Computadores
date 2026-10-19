
from cpu import CPU


def executar_programa(titulo, instrucoes):
    print("\n" + "=" * 45)
    print(f"  {titulo}")
    print("=" * 45)

    cpu = CPU()

    # Carrega as instruções na memória
    for idx, instrucao in enumerate(instrucoes):
        cpu.memoria[idx] = instrucao

    # Executa o programa
    cpu.executar()

    print("\n" + "=" * 45)
    print("RESULTADO FINAL DESSA EXECUÇÃO")
    print("=" * 45)
    cpu.mostrar_estado()
    
    # Exibe o conteúdo de posições alteradas na memória
    print("\nConteúdo da Memória (apenas valores gravados):")
    for pos, i in enumerate(cpu.memoria):
        if isinstance(i, int) and i != 0:
            print(f"  MEM[{pos:02d}] = {i:02X} ({i})")


# ======================================================
# 1. PROGRAMA DE EXEMPLO DO PROFESSOR (5 + 8 = 13)
# ======================================================
prog_exemplo = [
    "LOAD R0, 5",
    "LOAD R1, 8",
    "ADD R0, R1",
    "STORE R0, 15",
    "HALT"
]

# ======================================================
# 2. PROGRAMA PRÓPRIO (Mais de 8 instruções)
# Realiza operações de ADD, SUB, AND, OR e STORE em memória
# ======================================================
prog_proprio = [
    "LOAD R0, 12",    # R0 = 12
    "LOAD R1, 5",     # R1 = 5
    "ADD R0, R1",     # R0 = 12 + 5 = 17
    "SUB R0, R1",     # R0 = 17 - 5 = 12
    "LOAD R2, 3",     # R2 = 3
    "AND R2, R1",     # R2 = 3 AND 5 = 1
    "OR R0, R2",      # R0 = 12 OR 1 = 13
    "STORE R0, 14",   # Guardar R0 (13) no endereço 14 da memória
    "STORE R2, 15",   # Guardar R2 (1) no endereço 15 da memória
    "HALT"            # Parar execução
]


if __name__ == "__main__":
    # Executa o programa de exemplo
    executar_programa("PROGRAMA DE EXEMPLO (5 + 8)", prog_exemplo)

    # Executa o programa próprio exigido no trabalho
    executar_programa("PROGRAMA PRÓPRIO DE DEMONSTRAÇÃO", prog_proprio)