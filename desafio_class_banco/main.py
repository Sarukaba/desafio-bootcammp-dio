#desafio versão 2
from desafio_class_banco.utils.menu import menu
from desafio_class_banco.services.cliente_service import cadastrar_cliente, cadastrar_conta, deposito, saque, vizualizar_extrato
from typing import TYPE_CHECKING

if TYPE_CHECKING:
     from desafio_class_banco.models.clientes import Cliente
     from desafio_class_banco.models.contas import Conta

def main():
    user_cadastrados = []

    while True:

        opcao = input(menu())

        if opcao == "1":
            cliente = cadastrar_cliente(user_cadastrados)
            user_cadastrados.append(cliente)
        
        elif opcao == "2":
            print(cadastrar_conta(user_cadastrados))
            
        elif opcao =="3":
            deposito(user_cadastrados)


        elif opcao == "4":
            saque(user_cadastrados)

        elif opcao == "5":
            vizualizar_extrato(user_cadastrados)

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Por favor escolha um numero entre 1 e 6")
            

if __name__ == "__main__":
    main()
