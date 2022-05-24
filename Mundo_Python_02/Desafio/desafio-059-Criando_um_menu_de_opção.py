'''
Crie um programaque leia dois valores e mostre um menu como o ao lado da tela:
Seu programa devrárealizar a operação solicitada em cada caso.
'''

primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))

opcao = 0
maior = 0
while opcao != 5:
    print('      [ 1 ] Soma')
    print('      [ 2 ] Multiplicação')
    print('      [ 3 ] Maior')
    print('      [ 4 ] Novos Números')
    print('      [ 5 ] Sair do Programa')
    opcao = int(input('>>>>>>>> Qual é a sua opção?'))

    if opcao == 1:
        print(f'A soma entre {primeiro} + {segundo} = {primeiro + segundo}')
        print('=-'* 20)
    elif opcao == 2:
        print(f'A multiplicação entre {primeiro} x {segundo} = {primeiro * segundo}')
        print('=-' * 20)
    elif opcao == 3:
        if primeiro > segundo:
            maior = primeiro
            print(f'{primeiro} > {segundo}')
            print('=-' * 20)
        elif segundo > primeiro:
            maior = segundo
            print(f'{segundo} > {primeiro}')
            print('=-' * 20)
        elif primeiro == segundo or segundo == primeiro:
            print(f'{primeiro} = {segundo}')
            print('=-' * 20)
    elif opcao == 4:
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Volte Sempre!!!')
    elif opcao > 5:
        print('Informe uma opção Válida!!\n')
        print('      [ 1 ] Soma')
        print('      [ 2 ] Multiplicação')
        print('      [ 3 ] Maior')
        print('      [ 4 ] Novos Números')
        print('      [ 5 ] Sair do Programa')
        opcao = int(input('>>>>>>>> Qual é a sua opção?'))
