'''
Crie um progarama onde 4 jogadores joguem um dado e tenham resultados aleatórios. guarde esses resultados em um dicionário em ordem.
sabendo que o vencedor tirou maior número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter #funçao para colocar o dicionario em ordem
jogadores = {'jogador1': randint(1,6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)
             }
ranking = list()
print('Valores sorteados')
for chave, valor in jogadores.items():
    print(f'{chave} tirou {valor} no dado.')
    sleep(0.5)

print('-='*15)
print('=== Ranking dos Jogadores ===')
ranking = sorted(jogadores.items(),key=itemgetter(1),reverse=True) # colocar os valores em ordem
for numero,valor in enumerate (ranking):
    print(f'{numero+1}° lugar:{valor[0]} com {valor[1]}.')
    sleep(0.5)

