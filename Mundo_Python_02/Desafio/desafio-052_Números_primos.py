'''
Faça um programa que leia um número inteiro e diga se ele é ou nao um numero primo.
'''
cores = {'limpa':'\33[m',
         'azul':'\033[34m',
         'vermelho':'\033[31m'}
contador = 0
numero = int(input('Informe um numero inteiro: '))
for c in range(1, numero+1):
    if numero % c == 0:
        contador += 1
        print(f'{cores["vermelho"]}{c}{cores["limpa"]}',end='  ')
    else:
        print(f'{cores["azul"]}{c}{cores["limpa"]}', end='  ')
print('')
if contador == 2:
    print(f'\nO numero {numero} foi dividido {contador}x')
    print(f'É número PRIMO.')
else:
    print(f'\nO numero {numero} foi dividido {contador}x')
    print(f'Não é número PRIMO.')





