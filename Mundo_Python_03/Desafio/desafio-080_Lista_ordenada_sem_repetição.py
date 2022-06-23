'''
Crie um programa onde o usuario possa dogitar cindo valores numéricos e cadastrar-os em lista. ja na posiçção correta
de insserção(sem osar sort(). no dinal,mostre a lista ordenadana tela
'''

'''numeros = list()
for c in range(0,5):
    numero = (int(input(f'Digite um valor: ')))
    numeros.append(numero)
    numeros.sort()
    print(f'O valor {numero} foi adicionado na posição {numeros.index(numero)}')
print(numeros)'''

numeros = list()
for c in range(0,5):
    numero = int(input(f'Digite um valor: '))
    numeros.append(numero)
    maior = max(numeros)
    menor = min(numeros)
    print(numeros)
    print(maior)
    print(menor)




