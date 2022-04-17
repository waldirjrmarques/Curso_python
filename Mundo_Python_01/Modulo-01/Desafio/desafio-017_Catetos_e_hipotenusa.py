'''
faça um programa que leia o comprimento do cateto oposto e do catedo
adjacentede um triangulo. Calcule e mostre o comprimento da hipotenusa.
'''
# 1° Primeiro modo de fazer.
'''
C_oposto = float(input('Informe o valor do Cateto Oposto: '))
C_adjacente = float(input('Informe o valor do Cateto adjacente: '))
hipotenusa = (C_oposto ** 2 + C_adjacente ** 2 ) ** (1/2)
print('Cateto oposto {}\nCateto Adjacente {}\nHipotenusa {}'.format(C_oposto,C_adjacente,hipotenusa))
'''
#2° Segunda maneira: importando math
import math
C_oposto = float(input('Informe o valor do Cateto Oposto: '))
C_adjacente = float(input('Informe o valor do Cateto adjacente: '))
hipotenusa = math.hypot(C_oposto,C_adjacente)
print('Cateto oposto {}\nCateto Adjacente {}\nHipotenusa {}'.format(C_oposto,C_adjacente,hipotenusa))