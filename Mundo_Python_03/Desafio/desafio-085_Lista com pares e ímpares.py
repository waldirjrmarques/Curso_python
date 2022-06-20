'''
Crie um program onde o usuario possa digitar  7 valores numericos e cadastre-os em uma lista única
que mantenha separados os valores pares e impares.Nofinal,mostre os valores pares e impares
em ordem Crescente.
'''


par_impar = [[],[]]
for c in range(1,8):
    numero = int(input(f'Informe o {c}° Numero: '))
    if numero % 2 == 0:
        par_impar[0].append(numero)
    else:
        par_impar[1].append(numero)

par_impar[0].sort()
par_impar[1].sort()
print(par_impar)
print(f'Numeros pares Digitados{par_impar[0]}')
print(f'Numeros Ímpares Digitados {par_impar[1]}')

