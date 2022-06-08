'''
Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuario qual será o valor a ser sacado(numero inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

obs: Considere que o caixa possoui cédulas de
 - rR$:50
 - rR$:20
 - rR$:10
 - rR$:1
'''

print('='*30)
print(f'{"Banco CEV":^30}')
print('='*30)

valor = int(input('Que valor você quer sacar? R$: '))
ced = 50
totalced = 0
while True:
    if valor >= ced:
        valor -= ced
        totalced += 1
    else:
        if totalced > 0:
           print(f'Total de {totalced} cédulas de R${ced}')
        #condição mudar o valor da cedula
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        #faz nova contagem de cada condição
        totalced = 0
        if valor == 0:
            break

'''print('='*30)
print(f'{"Banco CEV":^30}')
print('='*30)


valor = int(input('Que valor você quer sacar? R$: '))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break

print('='*30)
print(f'{"Volte Sempre!!!":^30}')
print('='*30)
'''