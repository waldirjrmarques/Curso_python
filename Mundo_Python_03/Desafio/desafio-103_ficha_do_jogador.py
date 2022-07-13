'''
Faça um programa que tenha uma função chamada ficha(), que recebe dois parâmetros opcionais: o nome de um jogador e a quantos gols ele marcou. O programa
deverá ser capaz de mostrar informado corretamente.
'''
def ficha(n=True,g=True):

    
    if n and g:
        print(f'O jogador {n} fez {g} gol(s) no campeonato.')
    elif n:
        print(f'O jogador {n} fez {g} gol(s) no campeonato.')
    elif g:
        print(f'O jogador <Desconhcido> fez {g} gol(s) no campeonato.')
    else:
        print(f'O jogador <Desconhcido> fez {g} gol(s) no campeonato.')



nome =  str(input('Nome do Jogador: '))
gols =  str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

ficha(nome,gols)