'''
Crie um programa que leia o nome completo de um pessoa e mostre:
 * O nome com todas as letras maiúsculas
 * O nome com todas minusculas
 * Quantas letras ao todas (sem considerar espaços)
 * Quantas letras tem o primeiro nome
'''
#Qual seu nome completo: Waldir Junior Lobo Marques
nome = input('Qual seu nome completo? ')
print(f'Nome em maiúsculo: {nome.upper()}')
print(f'Nome em minusculo: {nome.lower()}')
print('Quantidade de letras sem espaços: ',len(''.join((nome.split()))))
print(f'Quantidade de letra no primeiro nome:{len((nome.split())[0])}')


#obs: 2 maneiras de se trabalhar com string na declaração 1° (f'texto {}') 2° ('texto',len(variavel.split())