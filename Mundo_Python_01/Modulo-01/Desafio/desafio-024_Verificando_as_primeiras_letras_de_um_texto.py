'''
 Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome '
 "santo"
'''

nome = input('Infomor o nome cidade:')
santo = nome.lstrip().capitalize().split()[0]
print('Santo' in santo)
