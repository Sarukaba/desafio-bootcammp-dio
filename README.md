# 💳 Sistema Bancário em Python

Este projeto é uma simulação simples de um sistema bancário feito em Python, com funcionalidades básicas como cadastro de clientes, criação de contas, depósitos, saques e visualização de extrato.

---

## 📋 Funcionalidades

### 1. Menu Interativo
O programa exibe um menu com as seguintes opções:
- `[1]` Cadastrar cliente
- `[2]` Cadastrar conta bancária
- `[3]` Depositar
- `[4]` Sacar
- `[5]` Ver extrato
- `[6]` Sair

---

### 2. Cadastro de Cliente
Função: `cadastro_cliente(lista_users_cadastrados)`
- Solicita nome, CPF, data de nascimento e endereço.
- Verifica se o CPF já está cadastrado.
- Calcula a idade com base no ano de nascimento.
- Retorna um dicionário com os dados do cliente.

---

### 3. Cadastro de Conta Bancária
Função: `cadastrar_conta(lista_users_cadastrados)`
- Solicita o CPF do cliente.
- Verifica se o CPF está cadastrado.
- Cria uma conta com senha, número de conta, agência, saldo inicial, limite e extrato.

---

### 4. Depósito
Função: `depositar(lista_contas_cadastradas)`
- Solicita CPF e senha para autenticação.
- Permite inserir um valor de depósito.
- Atualiza o saldo e registra o valor no extrato.

---

### 5. Saque
Função: `sacar(lista_contas_cadastradas)`
- Solicita CPF e senha para autenticação.
- Permite inserir um valor de saque.
- Verifica se há saldo suficiente.
- Atualiza o saldo e registra o saque no extrato.

---

### 6. Verificar Extrato
Função: `verificar_extrato(lista_contas_cadastradas)`
- Solicita CPF e senha para autenticação.
- Exibe o histórico de transações (depósitos e saques).

---

## 🧠 Observações Técnicas

- Os dados são armazenados em listas de dicionários em tempo de execução.
- Não há persistência em banco de dados ou arquivos.
- O CPF é usado como identificador único para clientes e
