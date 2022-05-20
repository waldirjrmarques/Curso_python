'''
Estrutura de repetição com teste lógico.
Usa-se essa condição quando nao se sabe quantas vezes vai se repetir uma situaçao.

white = enquanto
not = nao
'''

#Contagem de 1 a 10 com for
for c in range(1,10):
    print(c)
print('Fim')

#Contagem de 1 a 10 com while
c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')


#Repetição com uma confirmação
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')

#para e impar com while

n = 1
par = impar = 0
while n !=0:
    n = int(input('Digite um valor: '))
    if n != 0: 
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números Pares e {impar} números Ímpares')

