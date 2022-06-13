'''
Faça um programa que leia 5 valores numericos e guarde os em uma lista. Nofinal, mostre qual foi o maior e o
menor valor digitado e as suas prespectivas posições na lista
'''
valores = list()
for c in range(0,5):
    valores.append(int(input(f'Informe um valor para a posição {c}: ')))
print(valores)
maior = max(valores)
menor = min(valores)

print(f'O maior valor digitado foi {maior} nas posições:',end=' ')
for indice, valor in enumerate(valores):
    if valor == maior:
        print(f'{indice}..',end=' ')

print(f'\nO menor valor digitado foi {menor} nas posições:',end=' ')
for indice, valor in enumerate(valores):
    if valor == menor:
        print(f'{indice}..',end=' ')

