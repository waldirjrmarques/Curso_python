'''
Crie um programa que leia: - nome: - ano de nascimento: - carteira de trabalho (com idade) em  um dicionario sepor acaso a ctps
for diferente de zero, o dicionario receberá tabembém o ano de contratação e o salário. calcule e acrescente, alem da idade,
com quantos anos a essoa vai se aponsentar.

'''
from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: ')[:4])
dados['idade'] = date.today().year - nascimento
dados['ctps'] = int(input('Carteira de Trabalho: [0 nao tem] '))

if dados['ctps'] == 0:
    print('-=' * 30)
    for chave , valor in dados.items():
        print(f'- - {chave} tem o valor {valor}')
else:
    dados['contratacao'] = int(input('Ano de Contratação: ')[:4])
    dados['salario'] = float(input('Salário: R$: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - date.today().year )
    print('-=' * 30)
    for chave, valor in dados.items():
        print(f'- - {chave} tem o valor {valor}')

