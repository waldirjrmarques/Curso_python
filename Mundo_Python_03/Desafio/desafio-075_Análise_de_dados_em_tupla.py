'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde em uma tupla. No final mostre:
* - Quantas vezes apareceu o valor 9.
* - Em que posição foi digitado o primeiro valor 3:
* - Quais foram os numeros pares
'''

valores = (int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')))
print(f'Você digitou os valores: {valores}')
print(f'O valor 9 apareceu {valores.count(9)}')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}ª posição.')
else:
    print(f'O valor 3 não apareceu.')
print('Os valores pares foram: ',end='')
cont= 0
for n in valores:
    if n % 2 == 0:
        cont += 1
        print(n,end=' ')
print(f'\nOs  pares digitados foram: {cont} vezes')

