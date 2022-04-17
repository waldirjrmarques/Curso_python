'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele.
lendo o nome deles e escrevendo o nome do escolhido.
'''
import random
nome01 = input('Informe o nome do aluno:')
nome02 = input('Informe o nome do aluno:')
nome03 = input('Informe o nome do aluno:')
nome04 = input('Informe o nome do aluno:')
nome05 = input('Informe o nome do aluno:')
lista = [nome01,nome02,nome03,nome04,nome05]
escolido = random.choice(lista)
print('O aluno selecionado foi {}'.format(escolido))

'''
Obs: para criar uma lista no python usamos []
'''