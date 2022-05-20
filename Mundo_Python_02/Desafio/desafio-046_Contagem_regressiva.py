'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,Indo de 10 ate 0, com uma pausa de 1 segundo entre eles.
'''

n = int(input('Informe o tempo da contagem regressiva: '))
from time import sleep
for c in range(n, 0,-1):
    print(c)
    sleep(1)
print('Bummmmm! '*3)
