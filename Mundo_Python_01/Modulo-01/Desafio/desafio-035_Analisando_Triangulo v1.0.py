'''
Desenvolva um programa que leia o comprimento de três  retas e diga ao usuario se elas podeme ou nao formar um triangulo.
'''

l1 = float(input('Primeiro  segmento: '))
l2 = float(input('Segundo   segmento: '))
l3 = float(input('Terceiro  segmento: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Pode formar um triãngulo')
else:
    print('Não pode formar um Triãngulo')


