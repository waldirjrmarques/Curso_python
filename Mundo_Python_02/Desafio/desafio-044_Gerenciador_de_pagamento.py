'''
Elabore um programa que calcule o valor a ser pago por um produtor,considerando o seu preço normal e condições de pagamento:
{1} - Á vista dinheiro e cheque: 10% de desconto
{2} - Á vista no cartão:5% de desconto
{3} - Em até 2x no cartão: Preço normal
{4} - 3x no cartão: 20% de juros

'''

cores = {'limpa':'\33[m',
         'azul':'\033[34m',
         'vermelho':'\033[31m'}

print(f'{cores["azul"]}******************************{cores["limpa"]}')
print('   Gerenciador de Pagamento  ')
print(f'{cores["azul"]}******************************{cores["limpa"]}')

valor_produto = float(input('Informe o valor do produto:'))
print('''Opçaoes de pagamento:\n1- Á vista dinheiro e cheque: 10% de desconto\n2- Á vista no cartão:5% de desconto \n3- Em até 2x no cartão: Preço normal\n4 - 3x no carttão: 20% de juros''')
forma_pagamento = int(input('Informe a condição de pagamento: '))

if forma_pagamento == 1:
    valor_produto = valor_produto - (valor_produto * (10/100))
    print('\nOpção informada {1}: Á vista dinheiro e cheque: 10% de desconto')
    print(f'O valor do produto fica em R$:{valor_produto:.2f}')
elif forma_pagamento == 2:
    valor_produto = valor_produto - (valor_produto * (5/100))
    print('\nOpção informada {2}: Á vista no cartão:5% de desconto')
    print(f'O valor do produto fica em R$:{valor_produto:.2f}')
elif forma_pagamento == 3:
    parcela = valor_produto / 2
    print('\nOpção informada {3}: Em até 2x no cartão: Preço normal')
    print(f'O valor do produto fica em R$:{valor_produto:.2f}')
    print(f'Valor da parcelas 3x R$:{parcela}')
elif forma_pagamento == 4:
    valor_produto = valor_produto + (valor_produto * (20 / 100))
    parcela = valor_produto / 3
    print('\nOpção informada {4}: 3x no cartão: 20% de juros')
    print(f'O valor do produto fica em R$:{valor_produto:.2f}')
    print(f'Valor da parcelas 3x R$:{parcela}')
else:
    print(f'\nOpção informada {forma_pagamento}: {cores["vermelho"]}OPÇÃO INVALIDA!{cores["limpa"]}')
