'''
Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o
seu novo salário, com 15% de aumento.
'''

nome = input('Nome do Funcionario:')
salario = float(input('{} Quanto é seu salário? R$:'.format(nome)))

novosalario = salario + (salario * (15 / 100 ))

print('O SALARIO  DE {} COM 15% DE AUMENTO É R$:{}'.format(nome,novosalario))