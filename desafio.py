def menu():
    
    def menu_inicial():
        return """
        [1] cadastrar cliente
        [2] cadastrar conta bancária
        [3] Depositar
        [4] Sacar
        [5] Extrato
        [6] Sair
        => """

    return menu_inicial()
def cadastro_cliente(lista_users_cadastrados : list):
    nome = input('Digite seu nome -> ')
    cpf = input('Digite seu cpf(Apenas numeros) -> ')
    
    for user in lista_users_cadastrados:
        if cpf == user['cpf']:
            return 'cpf invalido.'

    data_nasc = input('Digite sua data de nascimento(apenas os numeros) ->')
    endereco = input('Digite seu endereço -> ')
    idade = 2025 - int(data_nasc[4:])

    if len(cpf) > 11 or len(cpf)< 11:
        return 'cpf invalido, tente novamente.'
    else:
        return {'id':len(lista_users_cadastrados) + 1,
                'user': nome, 
                'cpf':cpf, 
                'idade':idade,
                'endereco':endereco}
def cadastrar_conta(lista_users_cadastrados : list):
    cpf_user = input('Digite seu cpf ->')
    for usuarios in lista_users_cadastrados:
        
        if cpf_user == usuarios['cpf']:
            password_user = input('Crie uma senha de acesso -> ')
            nome = usuarios['user']
            numero_conta = usuarios['id']    
            
            return {'cpf':cpf_user,'password':password_user,
                    'usuario':nome,'agencia':'0001',
                    'id':numero_conta,'saldo':0.0,
                    'limite':750, 'extrato':[]}

        else:
            return 'Erro, cpf invalido'
def depositar(lista_contas_cadastradas : list):  
    print('Insira suas informações de login')
    cpf = input('Insira seu cpf -> ')
    password = input('insira sua senha de acesso -> ')

    for conta in lista_contas_cadastradas:
        
        if cpf == conta['cpf'] and  password == conta['password']:
           print(f'olá {conta['usuario']}, Seja bem vindo')
           valor_depositado = float(input('Insira o valor do deposito -> '))
           conta['saldo'] += valor_depositado
           conta['extrato'].append(valor_depositado)
           return '\nDeposito realizado'
            
        else:
           return '\nCpf ou senha invalído'
def sacar(lista_contas_cadastradas : list):
    print('Insira suas informações de login')
    cpf = input('Insira seu cpf -> ')
    password = input('insira sua senha de acesso -> ')

    for conta in lista_contas_cadastradas:
        
        if cpf == conta['cpf'] and  password == conta['password']:
           print(f'olá {conta['usuario']}, Seja bem vindo')
           valor_saque = float(input(f'saldo:{conta['saldo']}\n\nInsira o quanto deseja sacar -> '))
           
           if valor_saque > conta['saldo']:
               return 'Não é possivel realizar o saque, pois o valor excede seu saldo atual.'
           
           else:
                conta['saldo'] -= valor_saque
                conta['extrato'].append(0 - valor_saque)
                return '\nSaque realizado realizado'
        
        else:
           return '\nCpf ou senha invalído'
def verificar_extrato(lista_contas_cadastradas : list):
    print('Insira suas informações de login')
    cpf = input('Insira seu cpf -> ')
    password = input('insira sua senha de acesso -> ')

    for conta in lista_contas_cadastradas:

        if cpf == conta['cpf'] and  password == conta['password']:
            print(f'olá {conta['usuario']}, Aqui está o historico de seu extrato bancário')       
            
            for valor in conta['extrato']:
                if valor > 0:
                    print(f'Deposito de {valor}')
                elif valor < 0:
                    print(f'Saque de {valor}')
                else:
                    print('transação não reconhecida') #Em caso de NONE

def main():
    usuarios_cadastrados = [{'id': 1, 'user': 'joao', 'cpf': '14496245450', 'idade': 21, 'endereco': 'PE'}]
    contas_cadastradas = [{'cpf': '14496245450', 'password': '123', 'usuario': 'joao', 'agencia': '0001', 'id': 1, 'saldo': 600.0, 'limite': 750,'extrato':[200,400,-700,700]}]

    while True:

        opcao = input(menu())

        if opcao == '1':
            usuarios_cadastrados.append(cadastro_cliente(usuarios_cadastrados))

        elif opcao == '2':
            contas_cadastradas.append(cadastrar_conta(usuarios_cadastrados))
            print(contas_cadastradas)

        elif opcao == '3':
            print(depositar(contas_cadastradas))
        
        elif opcao == '4':
            print(sacar(contas_cadastradas))
        
        elif opcao == '5':
            verificar_extrato(contas_cadastradas)
        
        elif opcao == '6':
            print('Saindo...')
            break

        else:
            print('Por favor escolha um numero entre 1 e 6')

main()