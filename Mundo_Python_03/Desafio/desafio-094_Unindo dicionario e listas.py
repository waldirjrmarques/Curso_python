'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
todos os dicionarios em uma lista. No final, mostre:
A) Quantas pessoas cadastradas
B) A  média de idade.
C) uma lista com mulheres.
D) uma lista com idade acima da média
'''
dados = list()
pessoas = dict()
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    while pessoas['sexo'] != 'M' and pessoas['sexo'] != 'F':
        print('ERRO! Por Favor, digite apenas M ou F. ')
        pessoas['sexo'] = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    pessoas['idade'] = int(input('Idade: '))
    dados.append(pessoas.copy())

    resp = str(input('Quer continuar [S / N ] ')).strip().upper()[0]
    while resp != 'S' and resp != 'N':
        print('ERRO! Por Favor, digite apenas S ou N. ')
        resp = str(input('Quer continuar [S / N ] ')).strip().upper()[0]
    if resp == 'N':
        break

print('-='*30)
print(dados)
print('-='*30)

print(f'A) Ao todo temos {len(dados)} cadastradas.')
soma = 0
for c in dados:
    soma += c['idade']
    media = soma / len(dados)
print(f'B) A media de idade é de {media:.2f} anos')
print(f'C) As mulheres cadastradas foram ',end=' ')
for c in dados:
    if c['sexo'] == 'F':
        print(f'[{c["nome"]}]',end=' ')
print('D) Lista das pessoas que estão acima da média:')
for c in dados:
    if media < c['idade']:
        print(f'  Nome = {c["nome"]}; Sexo = {c["sexo"]}; Idade = {c["idade"]};')
