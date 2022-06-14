'''
Crie um programa que vai ler vários números e colcar em uma lista. Depois disso, mostre:
* - Quantos números foram digitados
* - A lista de valores, ordenada de forma descrescente
* - Se o valor 5 foi digitado e está ou não na lista.
'''
valores = list()

while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    resp = str(input('Quer continuar [S / N ] ')).strip().upper()[0]
    while resp != 'S' and resp != 'N':
        print('ERRO')
        resp = str(input('Quer continuar [S / N ] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 20)
print(f'Você digitou {len(valores)} elementos')
valores.sort()
valores.reverse()
print(f'Os valores em ordem descrencente são: {valores}')
if 5 in valores:
    print(f'O numero 5 faz parte da lista')
else:
    print('O numero 5 não faz parte da lista ')