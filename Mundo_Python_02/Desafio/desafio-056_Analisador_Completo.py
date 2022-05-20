'''
Desenvolva um programa que lea o nome,idade,e sexo de 4 pessoas. No final do programa ,mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres tem menos de 20 anos.

'''
#Calcular médi
soma = 0
media = 0
# Homem Mais velho
mais_velho = 0
nome_velho = ''
# Mulher menor 20 anos
menor20 = 0

for c in range (1, 5):
    print(f'------ {c}° Pessoa ------')
    nome = str(input('Nome: ')).capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo - [M / F]: ')[0]).upper()

    #Calcular média
    soma += idade
    media = soma / c

    #Homem Mais velho
    if idade > mais_velho and sexo == 'M':
        mais_velho = idade
        nome_velho = nome

    #Mulher menor 20 anos
    if sexo == 'F' and idade < 20:
        menor20 += 1

print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho é o {nome_velho} com {mais_velho} anos')
print(F'Ao todo são {menor20} mulheres com menos de 20 anos.')
