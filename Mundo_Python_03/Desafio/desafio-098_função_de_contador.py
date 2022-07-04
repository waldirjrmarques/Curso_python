'''
Faça um programa que tenha uma função chamada contador(), que receba três
parametros: inicio, fim e passa. Seu programa tem que realizar três contagem atravéz da função criada
'''
'''
from time import sleep
def contador(um,onze,dez,menosdois):
    print('-='*15)
    print(f'Contando de {um} até {onze - 1} de {um} em {um}')
    for c1 in range(um,onze,um):
        print(f'{c1}', end=' ')
        sleep(0.5)
    print('Fim!')

    print('-=' * 15)
    print(f'Contagem de {dez} até 0 de {menosdois * -1} em {menosdois * -1}')
    for c2 in range(dez, menosdois, menosdois):
        print(f'{c2}', end=' ')
        sleep(0.5)
    print('Fim!')

    print('-=' * 15)
    print('Agora é sua vez de personalizar a contagem! ')
    inicio = int(input('Inicio:'))
    fim = int(input('Fim:'))
    passo = int(input('Passo:'))
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} até {abs(passo)}')
    if passo == 0:
        passo = 1
    if inicio > fim:
        if passo >=0:
            passo = passo- (2*passo) #passando numero possitiva para negativo
        for c3 in range(inicio, fim, passo):
            print(f'{c3}', end=' ')
            sleep(0.5)
        print('Fim!')
    else:
        if inicio < fim:
            fim = fim + passo
        for c3 in range(inicio,fim,passo):
            print(f'{c3}',end=' ')
            sleep(0.5)
        print('Fim!')

um  = 1
onze = 11
dez = 10
menosdois = -2

contador(um,onze,dez,menosdois)'''

from time import sleep
def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='* 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(0.2)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.2)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.2)
            cont -= p
        print('Fim!')


contador(1,10,1)
contador(10,0,2)
print('-=' * 20)
print(f'Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio:'))
fim = int(input('Fim:'))
passo = int(input('Passo:'))
contador(inicio,fim,passo)



