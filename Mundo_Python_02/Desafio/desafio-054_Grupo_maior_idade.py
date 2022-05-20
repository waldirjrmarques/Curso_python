'''
Crie um programa que leia o ano de nascimento de uma pessoa. No final,
mostre quantas pessoas ja sao maiores  e menos de idade.
'''


from datetime import date
ano_atual = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    ano_nasc = int(input(f'Em que ano a {c}° pessoa masceu ?')[0:4])
    idade = ano_atual - ano_nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} Pessoas são Maiores de idade')
print(f'{menor} Pessoas são Menores de idade')