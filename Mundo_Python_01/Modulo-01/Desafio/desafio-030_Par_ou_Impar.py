'''
Crie um programa que leia um numero inteiro e mostre  na tela se ele e PAR ou IMPAR
'''
numero = int(input('Informe o numero: '))

if numero % 2 == 0:
 print(f'{numero} é PAR')
else:
 print(f'{numero} é IMPAR')