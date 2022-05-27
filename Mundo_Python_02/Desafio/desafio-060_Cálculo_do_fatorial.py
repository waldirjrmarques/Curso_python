'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
'''
'''
from math import factorial
numero = int(input('Calcular seu Fatorial: '))
print(f'{factorial(numero)}')
'''


numero = int(input('Calcular seu Fatorial: '))
from math import factorial
fato = factorial(numero)
numero += 1
while numero != 1:
    numero -= 1
    if numero != 1:
            print(numero,end=' x ')
    else:
            print(f'{numero} =', end=' ')
print(fato)


