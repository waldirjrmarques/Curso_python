'''
Faça um programa que leia o peso de cinco pessoas. No final,mostre qual foi o maior e o menor peso lidos. 
'''
contador = 0
maior = 0
menor = 0
while contador < 5:
    contador += 1
    peso = float(input(f'Peso da {contador}° pessoa: '))
    if contador == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi de {maior}Kg')
print(f'O maior peso lido foi de {menor}Kg')