'''
Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
'''

frase = str(input('Informe a frase ou palavra: ')).lower()
palavra = ''.join(frase.split())
invertido = palavra[::-1] # invete uma frase ou palavra.

if palavra == invertido:
    print('palíndromo')
else:
    print('Não é palidromo')

