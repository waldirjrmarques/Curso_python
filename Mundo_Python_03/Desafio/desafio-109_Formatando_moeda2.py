'''
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parametro a mais, informando se o valor retornado
por elas vai ser ou nao formatado pela função moeda(),desenvolvida no desafio 108.
'''

import moeda3

valor = float(input('Digite o preço: R$'))
print(f'A metade de {moeda3.moeda(valor)} é {moeda3.metade(valor)}')
print(f'A dobro de {moeda3.moeda(valor)} é {moeda3.dobro(valor)}')
taxa = int(input(f'{moeda3.moeda(valor)}  com aumento de %:'))
print(f'Com aumento de {taxa}% {moeda3.moeda(valor)} é {moeda3.aumentar(valor,taxa)}')
taxa = int(input(f'{moeda3.moeda(valor)}  com desconto de %:'))
print(f'Com desconto de {taxa}% {moeda3.moeda(valor)} é {moeda3.diminuir(valor,taxa)}')
