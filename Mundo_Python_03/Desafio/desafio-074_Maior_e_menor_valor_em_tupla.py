#MINHA SOLOÇÃO
'''
maior = 0
menor = 0
print('Os numeros Sorteados:',end=' ')
for c in range (0,5):
    from random import randint
    n = randint(1,10)
    print(n,end='  ')
    if c == 0:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(f'\nMaior numero :{maior}')
print(f'Menor numero: {menor}')
'''

#SOLUÇÃO GUANABARA
from random import randint
n = randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60)
print(f'Os valores sorteados: {n}')
print(f'O maior valor sorteado: {max(n)}')
print(f'O menor valor sorteado: {min(n)}')