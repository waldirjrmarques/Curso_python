'''
Faça um progarama que ajude um jogador da mega sena a criar palpites. O programavai perguntar
quantos jogos serão gerados e vai sortear 6 numeors entre1 e 60 para cada jogada. Cadastrando
tudo em um alista composta.
'''
print('-='* 30)
print(f'{"Jogo da Mega Sena":^60}')
print('-='* 30)

jogos = int(input('Quantos jogos  quer eu sorteie? '))
print('-='* 4,f'Sorteando {jogos} jogos','-='* 4)
jogo = list()
jogosmega = list()
numero : list()

from time import sleep
from random import randint
#Faz a quantidade de jogadas escolhida pelo usuario
for j in  range(0,jogos):
    #Sorteia 6 numeros de 1 a 60
    contador = 0
    while True:
        numero = randint(1,60)
        if numero not in jogo:
            jogo.append(numero)
            contador += 1
        if contador == 6:
            break
    jogo.sort()
    jogosmega.append(jogo[:])
    print(f'Jogo {j+1}°: {jogosmega[j]}')
    sleep(0.5)
    jogo.clear()

