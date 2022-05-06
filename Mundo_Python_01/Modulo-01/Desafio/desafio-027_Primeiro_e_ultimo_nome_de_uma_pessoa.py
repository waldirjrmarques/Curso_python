'''
Façã um programa que leia o nome completo de uma pessoa,
mostrando em seguida p primeiro e o ultimo nome separadamente.
'''

nome = str(input('esvreva seu nome completo: ')).strip()

print(nome.split())
print(f'Primeiro nome : {nome.split()[0]}')
print(f'Ultimo nome: {nome.split()[-1]}')