'''
Faça um programa que mostre a tabuada de varios numeros , um de cada vez , para cada valor digitado pelo usuario. O programa
será interrompido quando o número solilitado for negativo.
'''
while True:
    print('---' * 15)
    n = int(input('Digite um número para ver sua tabuada: '))
    cont = 0
    print('---' * 15)
    if n <= -1:
        break
    for c in range (1,11):
        cont += 1
        print(f'{n} x {cont} = {n*cont}')






