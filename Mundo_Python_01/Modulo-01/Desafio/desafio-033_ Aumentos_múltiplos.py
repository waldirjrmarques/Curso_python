'''
Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento.
Para sálario superiores a R$1.250,00, CALCULE UM AUMENTO DE 10%
Para os inferiores ou igual , o aumento de 15%
'''

salario =  float(input('Informe seu salário: '))

if salario > 1250:
    print(f'Seu novo salário é {salario +(salario * 10/100)}')
if salario <= 1250:
    print(f'Seu novo salário é {salario + (salario * 15 / 100)}')