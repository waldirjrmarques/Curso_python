'''
Faça um programa  que teha uma lista chamada Números e duas funçoes chmadas sorteia()  e somarpar(). A primeira função vai sortear 5 numeros e vai colocá-los
dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''
valores = []

def sorteio(*num):
    print(f'Sorteando {len(num)} valores da lista:', end='')
    for valor in num:
        print(f'{valor}', end='  ')
        valores.append(valor)
    print('PRONTO!')

from random import randint
sorteio(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))



def somapar(maior):
    soma = 0
    print(f'Somamndo os valores pares da lista {maior} temos',end=' ' )
    for valor in maior:
        if valor % 2 == 0:
            soma += valor
    print(soma)
somapar(valores)
