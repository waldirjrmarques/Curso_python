#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangemte desse angulo.

# 1° Maneira
import math
angulo = int(input('Informe o valor do Angulo:'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('Seno {:.2f}\nCosseno {:.2f}\nTangete {:.2f}'.format(seno,cosseno,tangente))

# 2° Maneira
from math import sin,cos,tan
angulo = int(input('Informe o valor do Angulo:'))
seno = sin(math.radians(angulo))
cosseno = cos(math.radians(angulo))
tangente = tan(math.radians(angulo))
print('Seno {:.2f}\nCosseno {:.2f}\nTangete {:.2f}'.format(seno,cosseno,tangente))
