'''
Crie um prgrama que leia varios numeros interos pelo teclado. O programa só vai parar quando o usuario digitar o valor 999,
 que é a condição de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (descondiderando a flag)
'''
n = 0
s = 0
cont = 0
while True:
    n = int( input('Digite um número (999 p/ parar): '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Foram digitados {cont} numeros\nA soma vale {s}')