'''
Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles
que forem pares. se o valor digitado for impar desconsidere-o.
'''
soma = 0
cont = 0
for c in range(1,7):
    n = int(input(f'Informque {c} nunmero: '))
    if n  %  2  == 0:
        soma += n
        cont += 1
print(f'Você digitou {cont} pares e a soma deles deu {soma}')

