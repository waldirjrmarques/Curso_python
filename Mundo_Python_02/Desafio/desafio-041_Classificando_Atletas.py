'''
A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de
um atletae mostre sua categoria de acordo com a idade:
-Até 9 anos:Mirim
-Até 14 anos: Infantil
-Até 19 anos:JUNIOR
-Até 25anos:Sênio
-Acima:master
'''

cores = {'limpa':'\33[m',
         'azul':'\033[34m'}

print(f'{cores["azul"]}******************************{cores["limpa"]}')
print('      Verificar Categoria   ')
print(f'{cores["azul"]}******************************{cores["limpa"]}')

ano = int(input('Qual seu ano de nascimento: '))

from datetime import date
atual = date.today().year
idade = atual - ano


if idade <= 9:
    print(f'Você tem {idade} anos.\nCetoria: Mirim')
elif idade > 9 and idade <= 14:
    print(f'Você tem {idade} anos.\nCetoria: Infantil')
elif idade > 14 and idade <= 19:
    print(f'Você tem {idade} anos.\nCetoria: Junior')
elif idade > 19 and idade <= 25:
    print(f'Você tem {idade} anos.\nCetoria: Sênio')
elif idade > 25:
    print(f'Você tem {idade} anos.\nCetoria: Master')
