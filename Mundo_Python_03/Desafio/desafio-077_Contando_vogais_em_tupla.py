'''
Crie um programa que tenha uma tupla com varias palavras. Deopis disso, você deve mostrar,para cada palvra,
quais são as suas vogais.
'''
palavras = ('APRENDER',
            'PROGRAMAR',
            'LINGUAGEM',
            'PYTHON',
            'CURSO',
            'GRATIS',
            'ESTUDAR',
            'PRATICAR',
            'TRABALHAR',
            'MERCADO',
            'PROGRAMADOR',
            'FUTURO')
print(palavras)
for palavra in palavras:
    print(f'\nNa palavra {palavra} Temos',end=' ')
    for letra in palavra:
        if letra in 'AEIOU': #verifica se tem as letras 'AEIOU' dentro da palavra
            print(f'{letra}',end=' ')
