#Crie um algoritmo que leia um numero e mostre o seu dobro,triplo e raiz quadrado.

n1 = float(input('Digite um Nomero: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)
print('O dobro de {} é {}.\nO triplo de {} é {}\nA raiz-Q  de {} é {:.3f}\n'.format(n1,dobro,n1,triplo,n1,raiz))