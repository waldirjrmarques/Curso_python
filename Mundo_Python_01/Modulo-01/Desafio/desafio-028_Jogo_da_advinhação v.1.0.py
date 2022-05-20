'''
Escreva um programa que faça o conputador "pensar"  em um numero interio entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
O programa deverá escrever na tela se o usuario venceu ou perdeu.
'''
print('=======================================================')
print('Vou pensar em um núnero entre 0 e 5. Tente adivinhar...')
print('=======================================================')

from random import randint
from time import sleep
maquina = randint(0,5) #sorteia um nomero entre esses ranges
numero = int(input('Digite o número que está pensando: '))


print('PROCESSANDO...')
sleep(2)
if numero == maquina:
    print('VOCÊ GANHOU!')
else:
    print('Maquina ganhou!')
