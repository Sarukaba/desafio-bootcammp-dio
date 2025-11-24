from typing import TYPE_CHECKING, List
from desafio_class_banco.models.clientes import PessoaFisica
from desafio_class_banco.models.contas import ContaCorrente
from desafio_class_banco.models.historico import Historico


if TYPE_CHECKING:
    from desafio_class_banco.models.clientes import Cliente
    from desafio_class_banco.models.contas import Conta

def cadastrar_cliente(lista_users_cadastrados: List) -> "Cliente":
    
    nome = input("Digite seu nome -> ")
    cpf = input("Digite seu cpf(Apenas numeros) -> ")
    
    if len(cpf) > 11 or len(cpf) < 11:
        return "cpf invalido, tente novamente."
    
    
    data_nasc = input("Digite sua data de nascimento(apenas os numeros) ->")
    endereco = input("Digite seu endereço -> ")
    id = len(lista_users_cadastrados) + 1
        
    """Verificar se o usuario estar cadastrado após a inserção de todos os dados para evitar que um
    usuario identifique que determinado cpf já foi cadastro mesmo sem ter acesso a ele"""
    
    for user in lista_users_cadastrados:
        if cpf == user.cpf:
            return "Credenciais inválidas."

    cliente = PessoaFisica(endereco,id,cpf,nome,data_nasc)
    return cliente

def cadastrar_conta(lista_clientes_cadastrados: List[PessoaFisica]):
    user_cpf = input("Me informe seu cpf: ")
    user_data_nasc = input("Me informe sua data de nascimento: ")
    
    for cliente in lista_clientes_cadastrados:
    
        if cliente.cpf == user_cpf and cliente.data_nasc == user_data_nasc:
            id = len(cliente.contas) + 1
            agencia = "0001"
            usuario = cliente
            historico = Historico()
            conta_cliente = ContaCorrente(id,agencia,usuario,historico)
            
            cliente.adicionar_contas(conta_cliente)
            
            return True
    else:
        return "Dados Invalídos"
    
def deposito(lista_clientes_cadastrados: List[PessoaFisica]):
    user_cpf = input("Me informe seu cpf: ")
    user_data_nasc = input("Me informe sua data de nascimento: ")

    for cliente in lista_clientes_cadastrados:
    
        if cliente.cpf == user_cpf and cliente.data_nasc == user_data_nasc:

            for valor in cliente.contas:
                print(valor)

            opcao_cliente = int(input("Qual conta deseja utilizar: ?"))
            conta_cliente = cliente.contas[opcao_cliente - 1]

            valor = int(input("Qual valor deseja depositar: ?"))
            conta_cliente.depositar(valor)
            print(conta_cliente.saldo)


def saque(lista_clientes_cadastrados: List[PessoaFisica]):
    user_cpf = input("Me informe seu cpf: ")
    user_data_nasc = input("Me informe sua data de nascimento: ")

    for cliente in lista_clientes_cadastrados:
    
        if cliente.cpf == user_cpf and cliente.data_nasc == user_data_nasc:

            for valor in cliente.contas:
                print(valor)

            opcao_cliente = int(input("Qual conta deseja utilizar?: "))
            conta_cliente = cliente.contas[opcao_cliente - 1]

            valor = int(input("Qual valor deseja sacar?: "))
            conta_cliente.sacar(valor)
            print(conta_cliente.saldo)

def vizualizar_extrato(lista_clientes_cadastrados: List[PessoaFisica]):
    user_cpf = input("Me informe seu cpf: ")
    user_data_nasc = input("Me informe sua data de nascimento: ")

    for cliente in lista_clientes_cadastrados:
    
        if cliente.cpf == user_cpf and cliente.data_nasc == user_data_nasc:

            for valor in cliente.contas:
                print(valor)

            opcao_cliente = int(input("Qual conta deseja utilizar?: "))
            conta_cliente = cliente.contas[(opcao_cliente - 1)]

            print(conta_cliente.historico)    
    