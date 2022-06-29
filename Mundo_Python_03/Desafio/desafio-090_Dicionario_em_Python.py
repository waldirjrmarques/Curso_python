'''
Faça um programa que leia nome  e média de um aluno, guardando também a situação em um dicionário.
No fina, mostre o conteúdo da estrutura na tela.
'''

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] >= 5 and aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('-='* 15)
for chave ,valor in aluno.items():
    print(f' -- {chave} é igual a {valor}')