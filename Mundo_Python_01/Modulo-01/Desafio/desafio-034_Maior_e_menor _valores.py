'''
Faça um programa que leia três numeros e mostre qual e o maior e qual e o menor.

#1° Maneira de fazer Maior

n1 = float(input('Informe o primeiro valor: '))
n2 = float(input('Informe o segundo valor: '))
n3 = float(input('Informe o terceiro valor: '))

if   n1 > n2 and n1 > n3:
    print(f'{n1} foi o maior numero digitado')
if n2 > n1 and n2 > n3:
    print(f'{n2} foi o maior numero digitado')
if n3 > n1 and n3 > n2:
    print(f'{n3} foi o maior numero digitado')
#Menor
if   n1 < n2 and n1 < n3:
    print(f'{n1} foi o menor numero digitado')
if n2 < n1 and n2 < n3:
    print(f'{n2} foi o menor numero digitado')
if n3 < n1 and n3 < n2:
    print(f'{n3} foi o menor numero digitado')'''

#2° Maneira de fazer.
n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
n3 = int(input('Informe o terceiro valor: '))

maior = n1
if n2 > n1 and n2 > n3:
     maior = n2
if n3 > n1 and n3 > n2:
     maior = n3
print(f'O maior numero digitado foi {maior}')

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O menor numero digitado foi {menor}')
