#Crie um programaque leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.

# 1° Sem a funçao math
numero = float(input('Informe um numero real: '))
print('O numero real é {}, Sua parte inteira é {} '.format(numero,int(numero)))

# 2° Modo de fazer: Chamando todas as funções da math
import math
numero = float(input('Informe um numero real: '))
print('O numero real é {}, Sua parte inteira é {} '.format(numero,math.trunc(numero)))

#3° Modo de fazer: Chamando a função especifica da math

from math import trunc
numero = float(input('Informe um numero real: '))
inteiro = trunc(numero)
print('O numero real é {}, Sua parte inteira é {} '.format(numero,inteiro))
