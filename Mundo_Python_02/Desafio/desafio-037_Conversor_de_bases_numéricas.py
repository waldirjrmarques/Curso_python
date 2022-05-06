'''
Escreva um programa que leia um numero inteiro qualquer e peça para p usuario escolher qual será a base de conversão:
1 - para binário
2 - para octal
3 - hexadecimal
'''

numero =  int(input('Informe um numero: '))
print('Escolha uma base para conversão: ')
print('[1] - para binário')
print('[2] - para octal')
print('[3]- hexadecimal')
opcao = int(input('Sua opção:'))

if   opcao == 1 :
    print(f'{bin(numero)[2:]}')
elif opcao == 2 :
    print(f'{oct(numero)[2:]}')
elif opcao == 3:
    print(f'{hex(numero)[2:]}')
else:
    print('ERRO')

