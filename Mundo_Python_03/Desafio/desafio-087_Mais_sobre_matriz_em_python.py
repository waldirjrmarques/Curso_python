'''
Aprimore o desafio 086 mostrando no final
* -A soma de todos os valores pares digitados
* -A soma da terceira coluna
* -O maior valor da segunda linha

'''
matriz = [[0, 0, 0],[0, 0, 0,],[0, 0 ,0]]
somapar = 0
somaultimacoluna = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Informe o [{linha}] [{coluna}] Numero: '))
    #Somar valores da coluna 3
    somaultimacoluna += matriz[linha][coluna]
print('-='* 30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end='')
        # somar valores par
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
    print()

print('--'* 15)
print(f'A soma dos valores pares é {somapar}')
print(f'A soma da ultima coluna é {somaultimacoluna}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')

