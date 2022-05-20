'''
Fça um progrma que leia o ano de nascimento de um jovem  e informe, de acordo com sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se ja passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo.
'''
cores = {'limpa':'\33[m',
         'azul':'\033[34m'}

print(f'{cores["azul"]}******************************{cores["limpa"]}')
print('      Alistamento Militar   ')
print(f'{cores["azul"]}******************************{cores["limpa"]}')

from datetime import date
ano_nascimento = int(input('Qual seu anos de nascimento? ')[0:4])
sexo = str(input('Qual seu sexo [F] ou [M]: ')).upper()

ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade < 18 and sexo == 'M':
    saldo = 18 - idade
    ano_alistamento = ano_atual + saldo
    print(f'Sua idade: {idade}\nAinda vai se alistar ao serviço militar, Falta {saldo} anos.')
    print(f'Seu alistamento vai sem em {ano_alistamento}')

elif idade == 18 and sexo == 'M':
    print(f'Sua idade: {idade}\n É a hora de se alistar ao serviço militar')

elif idade > 18 and sexo == 'M':
    saldo = idade - 18
    ano_alistamento = ano_nascimento + 18
    print(f'Sua idade: {idade}\nJá passou do tempo do alistamento, Já passou {saldo} anos.')
    print(f'Seu alistamento foi em {ano_alistamento}')

elif sexo == 'F':
    print('Sexo : FEMINITO.\nServiço militar não obrigatório.')

