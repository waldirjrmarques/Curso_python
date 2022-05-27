'''
Faça um programa que leia um numero interio e diga se ele é ou nao um
'''
termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
contador = 1

while contador <= 10:
    print(termo,end=' -> ')
    contador += 1
    termo = termo + razao
print('pausa')

mais = int(input('Quantos termos quer mostrar inda? '))
while mais != 0:
    for c in range(0,mais):
            print(termo, end=' -> ')
            termo = termo + razao
            contador += 1
    print('pausa')
    mais = int(input('Quantos termos quer mostrar inda? '))
print(f'\nProgressão finalizada com {contador} termos mostrados.')