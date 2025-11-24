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
Classe: `Cliente`
- Armazena nome, CPF, data de nascimento, idade e endereço.
- Verifica se o CPF já está cadastrado.
- Os objetos `Cliente` são adicionados a uma lista de clientes cadastrados.

---

### 3. Cadastro de Conta Bancária
Classe: `Conta` (abstrata) e subclasses como `ContaCorrente`
- Associada a um cliente existente.
- Possui atributos como número da conta, agência, saldo, limite e histórico.
- Cada conta é representada por um objeto e adicionada à lista de contas cadastradas.

---

### 4. Depósito
Método: `depositar(valor)`
- Solicita CPF e senha para autenticação.
- Permite inserir um valor de depósito.
- Atualiza o saldo e registra a transação como objeto `Deposito` no histórico da conta.

---

### 5. Saque
Método: `sacar(valor)`
- Solicita CPF e senha para autenticação.
- Permite inserir um valor de saque.
- Verifica se há saldo suficiente.
- Atualiza o saldo e registra a transação como objeto `Saque` no histórico da conta.

---

### 6. Verificar Extrato
Método: `extrato()`
- Solicita CPF e senha para autenticação.
- Exibe o histórico de transações (depósitos e saques) armazenados como objetos na lista de histórico da conta.

---

## 🧠 Observações Técnicas

- Os dados são armazenados em **objetos de classes** (`Cliente`, `Conta`, `Historico`, `Transacao`).
- Esses objetos são mantidos em listas (`clientes`, `contas`) durante a execução.
- Não há persistência em banco de dados ou arquivos.
- O CPF continua sendo usado como identificador único para clientes e contas.

        self.endereco = endereco
        self.contas = []

