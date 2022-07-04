'''
Faça um programa que tenha uma função chamada escreva(), que receba um texto qulquer como
parametro e mostre uma mensagem com tamanho adaptável.
'''

def escreva(msg):
    #variavel para ajustar a linha de acordo com a msg
    tamanho = len(msg) + 4

    print('~'* tamanho)
    print(f'  {msg}')
    print('~' * tamanho)

escreva(str(input('Escreva a menssagem: ')))


