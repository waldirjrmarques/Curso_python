'''
Melhore o jogo do desafio 028  onde o compuatador vai "pensar em um  numero entre 0 e 10. Sò que agora o
jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer."
'''
#Maneira que eu fiz
'''
print('Sou seu computador....')
print('Acabei de pensar em um número entre 0 e 10.')

from random import randint
maquina = randint(0,10) #sorteia um nomero entre esses ranges
palpite = 0
tentativa = 0
while palpite != maquina:
    tentativa += 1
    palpite = int(input('Qual seu palpite? '))
    if palpite > maquina:
            print('Menos...,Tente mais uma vez')
    elif palpite < maquina:
            print('Mais...,Tente mais uma vez')
print(f'Após  {tentativa} tentativas')
print(f'Você acertou!!!  Maquina {maquina} x {palpite} Jogador ')
'''

#maneira que guanabata fez

print('Sou seu computador....')
print('Acabei de pensar em um número entre 0 e 10.')

from random import randint
maquina = randint(0,10) #sorteia um nomero entre esses ranges
acertou = False
jogador = 0
tentativa = 0
while not acertou:
    tentativa += 1
    jogador = int(input('Qual seu palpite? '))
    if jogador == maquina:
        acertou = True
    else:
        if jogador > maquina:
            print('Menos...,Tente mais uma vez')
        elif jogador < maquina:
            print('Mais...,Tente mais uma vez')

print(f'Após  {tentativa} tentativas')
print(f'Você acertou!!!  Maquina {maquina} x {jogador} Jogador ')





