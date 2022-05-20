'''
Faça o desafio 009, mostrando a tabuada, só que agora utilizando um laço for
'''
n = int(input('Digite um número para ver sua tabuada: '))
cont = 0
for c in range (1,11):
    cont += 1
    print(f'{n} x {cont} = {n*cont}')