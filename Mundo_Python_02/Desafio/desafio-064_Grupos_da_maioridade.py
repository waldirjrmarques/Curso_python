'''
Crie um programa que leia o ano de nascimento de 7 pessoas sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date
contador = 0
menor = 0
maior = 0
while contador < 7:
    contador += 1
    ano_atual = date.today().year
    ano = int(input(f'Em que ano a {contador}° pessoa nasceu?').strip()[:4])
    idade = ano_atual - ano
    if idade < 18:
        menor += 1
    else:
        maior += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade.')
print(f'Ao todo tivemos {menor} pessoas menores de idade.')
