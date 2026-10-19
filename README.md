# CPU Simulada de 8 bits em Python

Trabalho Prático da disciplina de **Arquitetura de Computadores (AOC - 2026.2)**  
**Universidade Federal do Ceará (UFC) – Campus Sobral**  
**Professor:** Wendley S. Silva  

---

##  Visão Geral do Projeto

Este projeto consiste na implementação de um modelo didático e executável de uma **CPU de 8 bits** desenvolvida em Python. O objetivo principal é simular o funcionamento interno de um processador integrando conceitos de:
- Unidade Lógica e Aritmética (**ULA**)
- Banco de Registradores (**R0**, **R1**, **R2**, **R3**)
- Contador de Programa (**PC**)
- Memória Principal (16 posições)
- Ciclo de instrução **Fetch → Decode → Execute**

---

##  Arquitetura do Processador

| Componente | Especificação |
| :--- | :--- |
| **Tamanho dos Dados** | 8 bits (valores delimitados entre `0` e `255` / `0x00` e `0xFF`) |
| **Registradores Gerais** | `R0`, `R1`, `R2`, `R3` |
| **Contador de Programa** | `PC` (aponta para a instrução atual na memória) |
| **Memória Principal** | 16 posições (`MEM[0]` a `MEM[15]`) |
| **ULA** | Suporte a `ADD`, `SUB`, `AND`, `OR`, `XOR` |
| **Ciclo de Execução** | Fetch → Decode → Execute |

---

##  Conjunto de Instruções

| Instrução | Exemplo | Descrição |
| :--- | :--- | :--- |
| **LOAD** | `LOAD R0, 5` | Armazena o valor imediato `5` no registrador `R0`. |
| **STORE** | `STORE R0, 15` | Grava o valor contido em `R0` na posição `15` da memória. |
| **ADD** | `ADD
