'''
Faça um programa que leia o sexo de uma pessoa , mas só aceite os  valores 'M' ou F.
Caso esteja errado, peça a digitação novamente até um valor coreto.
'''

sexo = ''
sexo = str(input('Qual é seu sexo [M / F]: ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    if sexo != 'M' and sexo != 'F':
        sexo = str(input('Dados inválidos. Por Favor, Qual é seu sexo [M / F]: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')
