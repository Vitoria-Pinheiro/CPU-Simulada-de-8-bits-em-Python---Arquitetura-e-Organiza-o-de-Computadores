
from cpu import CPU


def executar_programa(titulo, instrucoes):
    print("\n" + "=" * 45)
    print(f"  {titulo}")
    print("=" * 45)

    cpu = CPU()

    
    for idx, instrucao in enumerate(instrucoes):
        cpu.memoria[idx] = instrucao

   
    cpu.executar()

    print("\n" + "=" * 45)
    print("RESULTADO FINAL DESSA EXECUÇÃO")
    print("=" * 45)
    cpu.mostrar_estado()
    
    
    print("\nConteúdo da Memória (apenas valores gravados):")
    for pos, i in enumerate(cpu.memoria):
        if isinstance(i, int) and i != 0:
            print(f"  MEM[{pos:02d}] = {i:02X} ({i})")



prog_exemplo = [
    "LOAD R0, 5",
    "LOAD R1, 8",
    "ADD R0, R1",
    "STORE R0, 15",
    "HALT"
]


prog_proprio = [
    "LOAD R0, 12",   
    "LOAD R1, 5",    
    "ADD R0, R1",     
    "SUB R0, R1",     
    "LOAD R2, 3",     
    "AND R2, R1",     
    "OR R0, R2",      
    "STORE R0, 14",   
    "STORE R2, 15",   
    "HALT"            
]


if __name__ == "__main__":
    
    executar_programa("PROGRAMA DE EXEMPLO (5 + 8)", prog_exemplo)

    
    executar_programa("PROGRAMA PRÓPRIO DE DEMONSTRAÇÃO", prog_proprio)
