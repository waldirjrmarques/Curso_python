#Sem importação de modulos.
'''
Sem modulo
num = int(input('Digite um numero: '))
raizq = num ** (1/2)
print('A raiz quadrada é {}'.format(raizq))
'''

#Com inportação de todas as funcionalidades do Módulo
'''
import math
num = int(input('Digite um numero: '))

raizq = math.sqrt(num)
print('A raiz de {} e igual a {}'.format(num,math.ceil(raizq)))
'''
#Com importação especificas de funções do mudulo.

from math import sqrt,floor
num = int(input('Digite um numero: '))
raizq = sqrt(num)
print('A raiz de {} é igual a {}'.format(num,floor(raizq)))
