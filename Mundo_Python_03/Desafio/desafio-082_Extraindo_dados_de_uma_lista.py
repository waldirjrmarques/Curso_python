'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas estras que vão
contar apenas os valores pares eos valores impares digitados,respectivamente. Ao final, mostre o contéudo das três listas geradas.
'''
valores = list()
pares = list()
impar = list()
while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impar.append(valor)
    resp = str(input('Quer continuar [S / N ] ')).strip().upper()[0]
    while resp != 'S' and resp != 'N':
        print('ERRO')
        resp = str(input('Quer continuar [S / N ] ')).strip().upper()[0]
    if resp == 'N':
        break

print('-=' * 20)
print(f'A lista Completa {valores}')
print(f'A lista Pares {pares}')
print(f'A lista Impar {impar}')