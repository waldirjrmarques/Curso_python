'''
Crie um programa ond o usuário digite uma expressão qualquer que use parenteses. Seu aplicativo deverá analisar se a expressão passada
está com os parênteses abertos e fechados na ordem correta
'''
cont = 0
expresssao = list(str(input('Digite sua expressao: ')))
print(expresssao)

for indice, valor in enumerate(expresssao):
    '''print(f'No indice {indice} encontrei o valor {valor}')'''
    if '(' in valor:
        cont += 1
    if ')' in valor:
        cont -= 1
if cont == 0:
    print('Expressão Válida!')
else:
    print('Expressão Inválida')