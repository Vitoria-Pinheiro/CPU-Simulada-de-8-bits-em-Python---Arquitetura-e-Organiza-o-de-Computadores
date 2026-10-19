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

## Como Executar o Projeto

### Pré-requisitos

- **Python 3.8 ou superior** instalado na máquina.
- Nenhuma biblioteca externa é necessária; o projeto usa apenas a biblioteca padrão do Python.

Para verificar a versão instalada:

```bash
python --version
```

> No Linux/macOS, pode ser necessário usar `python3` no lugar de `python`.

### Passo a passo

**1. Clone o repositório**

```bash
git clone https://github.com/<seu-usuario>/<nome-do-repositorio>.git
cd <nome-do-repositorio>
```

Se preferir, baixe o projeto como `.zip` pelo GitHub, extraia e abra a pasta no terminal.

**2. Execute a CPU**

```bash
python main.py
```

**3. Acompanhe a saída**

O simulador executa o programa carregado na memória, ciclo a ciclo (Fetch → Decode → Execute), e exibe no terminal o estado do `PC`, dos registradores `R0` a `R3` e da memória.

### Executando seu próprio programa

Para testar outras instruções, edite o programa carregado na memória dentro do arquivo `main.py` e execute novamente. Exemplo:

```text
LOAD R0, 5
LOAD R1, 3
ADD R0, R1
STORE R0, 15
HALT
```

Ao final, `MEM[15]` deve conter o valor `8`.

### Problemas comuns

| Problema | Solução |
| :--- | :--- |
| `python: command not found` | Use `python3 main.py` ou instale o Python em [python.org](https://www.python.org/downloads/). |
| `No such file or directory` | Verifique se você está dentro da pasta do projeto (`cd <nome-do-repositorio>`). |
