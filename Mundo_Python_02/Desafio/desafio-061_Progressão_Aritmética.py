'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.No final, mostre os 10 primeiros termos dessa progressão.
com repetição while
'''
'''
termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
decimo = termo + (10-1) * razao
for c in range(termo, decimo, razao):
    print(c, end='--> ')
print('Acabou.')
'''

termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
contador = 1

while contador <= 10:
    print(termo,end=' -> ')
    contador += 1
    termo = termo + razao
print('Acabou')




