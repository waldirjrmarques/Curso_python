'''
Escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma mensagem.
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior. Os dois são iguais.
'''
cores = {'limpa':'\33[m',
         'azul':'\033[34m'}

print(f'{cores["azul"]}******************************{cores["limpa"]}')
print('      Analise de Numeros')
print(f'{cores["azul"]}******************************{cores["limpa"]}')

n1 = int(input('Informe o primeiro numero:'))
n2 = int(input('Informe o segundo numero:'))

if n1 > n2:
    print(f'O primeiro valor é maior')
elif n2 > n1:
    print(f'O segundo valor é maior')
else:
    print('Não existe valor maior. Os dois são iguais')
