'''Faça um algoritmo que leia a largura e altura de uma parede, calcule e
mostre a área a ser pintada e a quantidade de tinta necessária para o serviço,
sabendo que cada litro de tinta pinta uma área de 2metros quadrados.'''

altura = float(input('QUAL A ALTURA DA PAREDE: '))
largura = float(input('QUAL A LARGURA DA PAREDE: '))

metroq = altura * largura
LITRO_TINTA = 2
QUANT_LITRO = metroq / LITRO_TINTA

print('A ÁREA A SER PINTADA É DE: {} M2'.format(metroq))
print('SERÁ NECESSARIO {} LITROS DE TINTA PARA PINTAR {} M2.'.format(QUANT_LITRO,metroq))