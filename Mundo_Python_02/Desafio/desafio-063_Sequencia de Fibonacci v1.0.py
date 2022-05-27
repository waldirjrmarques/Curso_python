'''
Escreva um programa que leia um número n  inteiro qualquer e mostre na tela os n prineiros alementos de uma sequencia de fibonacci.

obs:a matemática, a sucessão de Fibonacci, é uma sequência de números inteiros, começando normalmente por 0 e 1,
na qual cada termo subsequente corresponde à soma dos dois anteriores.
p = 0
s = 1
t = p + s

p = s
s = t

'''

termo = int(input('Quantos termos quer mostar: '))

primeiro = 0
segundo = 1
print(primeiro,end=' -> ')
print(segundo,end=' -> ')

contador = 3
while contador <= termo:
    contador += 1
    terceiro = primeiro + segundo
    print(terceiro,end=' -> ')
    primeiro = segundo
    segundo = terceiro
print('Fim')



