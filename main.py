saldo = 1000

while True:
    print('\n === Caixa Eletrônico ===')
    print('1 - Consultar Saldo')
    print('2 - Depositar')
    print('3 - Sacar')
    print('4 - Sair')
        
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        print(f'\nSeu saldo é de: R$ {saldo:.2f}')

    elif opcao == '2':
        deposito = float(input('\nQuanto deseja depositar? R$ '))
        saldo += deposito
        print(f'Depósito realizado. Novo saldo: R$ {saldo:.2f}')

    elif opcao == '3':
        saque = float(input('\n Quanto deseja sacar? R$ '))

        if saque > saldo: 
            print('Saldo insuficiente.')
        else:
            saldo -= saque
            print(f'Saque realizado com sucesso. Novo saldo: R$ {saldo:.2f}')

    elif opcao == '4':
        print('\nObrigado por utilizar nosso banco.')
        break
    
    else:
        print('\nOpção inválida. Tente novamente.')