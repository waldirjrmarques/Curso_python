'''
Crie um programa que tenha uma função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa,
retornando um voto literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓTIO nas eleiçôes.
'''

def voto(ano):
    '''
    :param v:
    :return:
    '''
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return (f'Idade {idade} Não Vota!')
    elif 16 <= idade < 18 or idade > 65:
        return (f'Idade {idade} Voto Opçional!')
    else:
        return (f'Idade {idade} Voto Obrigatório!')

ano = int(input('Qual ano você nasceu? ')[:4])

#retorno da funçao
print(voto(ano))