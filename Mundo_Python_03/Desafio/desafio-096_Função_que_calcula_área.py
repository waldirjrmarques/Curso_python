'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno
'''
#01 criar a função
def area(larg,comp):
    a = larg * comp
    print(f'A área de um Terreno {larg} L x {comp} C é de {a}m²')

#02 - informando os valores
l = float(input('Largura:'))
c = float(input('Comprimento:'))
#03 - passando os valores para a função
area(l,c)