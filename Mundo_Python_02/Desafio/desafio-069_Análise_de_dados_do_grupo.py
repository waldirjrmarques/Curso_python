'''
Crie Um programa que leia a idade e o sexo de várias pessoas. a cada pessoa cadastrada. o programa deverá pergntar se o
usuario quer ou nao continuar.No final,mostre:
* - Quantas pessoas tem maiores de 18 anos
* - Quantos homens foram cadastrados.
* - Quantas mulheres tem menos de 20 anos.
'''
maior18 = 0
homens = 0
menor20 = 0
while True:
    print('--'*15)
    print('CADASTRO DE UMA PESSOA')
    print('--'*15)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [F / M]')).strip().upper()[0]
    #Se o sexo for != de masculino ou feminino
    if sexo != 'F' and sexo != 'M':
        print(f'Sexo Inválido: {sexo} ')
        sexo = str(input('Sexo: [F / M]')).strip().upper()[0]
    # Maior de 18 anos
    if idade >= 18:
        maior18 += 1
    # Homemns cadastrados
    if sexo == 'M':
        homens += 1
    #mulher menor de 20 anos
    if sexo == 'F' and idade < 20:
        menor20 += 1
    #break para parar o programa
    stop = str(input('Quer continuar? [S / N]')).strip().upper()[0]
    if stop == 'N':
        break

print(f'Total de pessoa mair de 18 anos: {maior18}')
print(f'Total de Homens cadastrados: {homens}')
print(f'Mulheres com menos de 20 anos: {menor20}')