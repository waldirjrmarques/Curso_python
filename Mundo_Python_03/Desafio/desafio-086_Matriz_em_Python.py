'''
Crie um programa que crie uma matriz de dimenlçao 3x3 e preencha com valores lido pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
'''

matriz = [[0, 0, 0],[0, 0, 0,],[0, 0 ,0]]
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Informe o [{linha}] [{coluna}] Numero: '))

print('-='* 30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end='')
    print()

