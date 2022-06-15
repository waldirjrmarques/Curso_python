'''
Crei um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista. Caso
o numero já exista la dentro, ele não será adicionadoo numero já exista la dentro, ele não será adicionado.
No final, serão exibidos todos os valores unicos digitalizados, em ordem crescente

'''
continuar = ''
numeros = list()
while True:
    numero = (int(input(f'Digite um valor: ')))

    if numero not in numeros: #Verifica  se nao  tem o numero na lista , se nao tiver adiciona.
        numeros.append(numero)
        print(f'Valor {numeros} adicionado com sucesso...')
        continuar = str(input('Quer Continuar [S / N]: ')).strip().upper()[0]
    else:
        print('Valor Duplicado.Não vai adicionar.')

    while continuar not in 'SN':
        print(f'Você digitou a Opção Inválida ')
        continuar = str(input('Quer Continuar [S / N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('=='* 20)
numeros.sort()
print(F'Valores adicionados na lista:{numeros}')


