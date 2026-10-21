
from cpu import CPU


def teste_load():
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 25"
    cpu.memoria[1] = "HALT"
    cpu.executar()

    assert cpu.registradores["R0"] == 25
    print("[OK] LOAD")


def teste_store():
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 42"
    cpu.memoria[1] = "STORE R0, 10"
    cpu.memoria[2] = "HALT"
    cpu.executar()

    assert cpu.memoria[10] == 42
    print("[OK] STORE")


def teste_ula_aritmetica():
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 15"
    cpu.memoria[1] = "LOAD R1, 5"
    cpu.memoria[2] = "ADD R0, R1"  
    cpu.memoria[3] = "SUB R1, R0"  
    cpu.memoria[4] = "HALT"
    cpu.executar()

    assert cpu.registradores["R0"] == 20
   
    assert cpu.registradores["R1"] == 241
    print("[OK] ULA (ADD e SUB)")


def teste_ula_logica():
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 12" 
    cpu.memoria[1] = "LOAD R1, 5"  
    cpu.memoria[2] = "AND R0, R1"  
    cpu.memoria[3] = "LOAD R2, 10" 
    cpu.memoria[4] = "OR R2, R1"   
    cpu.memoria[5] = "XOR R1, R1"  
    cpu.memoria[6] = "HALT"
    cpu.executar()

    assert cpu.registradores["R0"] == 4
    assert cpu.registradores["R2"] == 15
    assert cpu.registradores["R1"] == 0
    print("[OK] ULA (AND, OR e XOR)")


def teste_jmp():
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 10"
    cpu.memoria[1] = "JMP 4"
    cpu.memoria[2] = "LOAD R0, 99"
    cpu.memoria[3] = "HALT"
    cpu.memoria[4] = "LOAD R1, 20"
    cpu.memoria[5] = "HALT"
    cpu.executar()

    assert cpu.registradores["R0"] == 10
    assert cpu.registradores["R1"] == 20
    print("[OK] JMP")


def teste_halt():
    cpu = CPU()
    cpu.memoria[0] = "HALT"
    cpu.executar()

    assert cpu.halted is True
    print("[OK] HALT")


def teste_programa_exemplo():
    
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 5"
    cpu.memoria[1] = "LOAD R1, 8"
    cpu.memoria[2] = "ADD R0, R1"
    cpu.memoria[3] = "STORE R0, 15"
    cpu.memoria[4] = "HALT"
    cpu.executar()

    assert cpu.memoria[15] == 13
    print("[OK] Programa Exemplo (MEM[15] == 13)")


def teste_limite_8bits():
    
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 200"
    cpu.memoria[1] = "LOAD R1, 100"
    cpu.memoria[2] = "ADD R0, R1" 
    cpu.memoria[3] = "HALT"
    cpu.executar()

    assert cpu.registradores["R0"] == 44
    print("[OK] Limite de 8 bits (& 0xFF)")


if __name__ == "__main__":
    print("Executando bateria completa de testes...")
    print("---------------------------------------")

    teste_load()
    teste_store()
    teste_ula_aritmetica()
    teste_ula_logica()
    teste_jmp()
    teste_halt()
    teste_programa_exemplo()
    teste_limite_8bits()

    print("---------------------------------------")
    print("Todos os testes foram aprovados com sucesso!")
