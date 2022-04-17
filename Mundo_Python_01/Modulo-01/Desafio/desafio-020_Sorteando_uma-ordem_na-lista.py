'''
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro açunos e mostre a ordem sorteada.
'''

import random
nome01 = input('Informe o nome do aluno:')
nome02 = input('Informe o nome do aluno:')
nome03 = input('Informe o nome do aluno:')
nome04 = input('Informe o nome do aluno:')

lista = [nome01,nome02,nome03,nome04]
random.shuffle(lista)
print(lista)
