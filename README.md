# Gerador e Verificador de CPF em Python

Este projeto contém dois scripts principais em Python: um para gerar números de CPF válidos e outro para verificar a validade de um número de CPF fornecido. Além disso, uma interface gráfica foi criada com `tkinter` para facilitar a interação com esses scripts.

## Estrutura do Projeto

- `gerador_cpf.py`: Gera números de CPF válidos com base nas regras brasileiras de formação de CPFs.
- `verificador_cpf.py`: Verifica a validade de um número de CPF fornecido.
- `interface.py`: Interface gráfica utilizando `tkinter` para facilitar a interação com os scripts de geração e verificação de CPF.

## Requisitos

- Python 3.x
- Biblioteca `tkinter` (inclusa nas instalações padrão do Python)

Nenhuma outra biblioteca externa é necessária para executar os scripts.

## Como Usar

1. **Gerar um CPF**
   - Execute o script `gerador_cpf.py`:
     ```bash
     python gerador_cpf.py
     ```
   - O script exibirá um número de CPF gerado aleatoriamente e válido.

2. **Verificar um CPF**
   - Execute o script `verificador_cpf.py` e insira o CPF para validação:
     ```bash
     python verificador_cpf.py
     ```
   - O script informará se o CPF é válido ou não com base nas regras de formação do CPF.

3. **Interface Gráfica**
   - A interface `interface.py` foi desenvolvida com `tkinter`, permitindo a interação com as funcionalidades de geração e verificação de CPF em uma janela gráfica.
   - Execute o script `interface.py`:
     ```bash
     python interface.py
     ```
   - Siga as instruções na interface para escolher entre gerar ou verificar um CPF.

## Funcionamento dos Scripts

- **Geração de CPF**: O script de geração utiliza as regras do cálculo do dígito verificador para criar números de CPF válidos.
- **Verificação de CPF**: O script de verificação valida o CPF com base no algoritmo que calcula e confere os dígitos verificadores.
