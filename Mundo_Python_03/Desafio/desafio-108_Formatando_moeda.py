'''
Adapte o código do desafio 107 , criando uma função adcional chamada moeda()2 que consiga mostrar os valores com um valor monetário formatado.
'''

import moeda2

valor = float(input('Digite o preço: R$'))
print(f'A metade de {moeda2.moeda(valor)} é {moeda2.moeda(moeda2.metade(valor))}')
print(f'A dobro de {moeda2.moeda(valor)} é {moeda2.moeda(moeda2.dobro(valor))}')
taxa = int(input(f'{moeda2.moeda(valor)}  com aumento de %:'))
print(f'Com aumento de {taxa}% {moeda2.moeda(valor)} é {moeda2.moeda(moeda2.aumentar(valor,taxa))}')
taxa = int(input(f'{moeda2.moeda(valor)}  com desconto de %:'))
print(f'Com desconto de {taxa}% {moeda2.moeda(valor)} é {moeda2.moeda(moeda2.diminuir(valor,taxa))}')
