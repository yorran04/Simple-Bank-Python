menu = '''
[d] Deposito
[s] Saque
[e] Extrato
[x] Saír
=>  '''

saldo = 0
extrato = ''
limite = 500
numero_saque = 0
LIMITE_MAX_SAQUE = 3

while True:
    
    opcoes =input(menu)

    if opcoes == 'd' or opcoes == 'D':
        valor = float(input('Informe o valor de deposito: R$ '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        
        else:
            print('Operação falhou! o valor informado é inválido')
    
    elif opcoes == 's' or opcoes == 'S':
        valor = float(input('Informe o valor de saque: R$ '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saque >= LIMITE_MAX_SAQUE

        if excedeu_saldo:
            print('Operação não realizada! Seu saldo é insuficiente. ')

        elif excedeu_limite:
            print('Operação não realizada! O valor de saque excede o limite. ')

        elif excedeu_saques:
            print('Operação não realizada! Número máximo de saques excedido. ')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saque += 1

        else: 
            print('Operação não realizada! O valor informado é inválido ')

    elif opcoes == 'e' or opcoes == 'E':
        print('\n******************Extrato******************')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\n Saldo: R$ {saldo:.2f}')
        print('*********************************************')
        
    elif opcoes == 'x' or opcoes == 'x':
        break

    else:
        print('Opção invalida. Por favor selecionar novamente as opções desejada. ')



