'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA"  no nome.

'''

nome = input('Informe seu nome completo:')
silva = nome.strip().upper().split()
print('Seu nome tem silva? {}'.format('SILVA' in silva))
