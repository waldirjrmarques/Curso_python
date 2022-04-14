'''Crie um programa que leia o preço de um produto, calcule e mostre o seu
PREÇO PROMOCIONAL, com 5% de desconto.'''

produto = (input('QUAL PRODUTO DESEJA COMPRAR?'))
valor = float(input('QUAL O VALOR DO PRODUTO R$:'))

desconto = valor - (valor*(5/100))

print('O PRODUTO: {} É R$:{} COM DESCONTO DE 5% FICA POR R$:{}'.format(produto,valor,desconto))