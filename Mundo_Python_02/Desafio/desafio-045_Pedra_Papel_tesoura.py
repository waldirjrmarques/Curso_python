'''
Crie um programa que faça o computador jogar jokenpô com você
'''
cores = {'limpa':'\33[m',
         'azul':'\033[34m',
         'vermelho':'\033[31m'}

print(f'{cores["azul"]}*********************************{cores["limpa"]}')
print(' GAMER : Pedra - Papel - Tesoura  ')
print(f'{cores["azul"]}*********************************{cores["limpa"]}')

from random import randint
maquina =('Pedra', 'Papel', 'Tesoura')
maquina = (randint(0,2))

print('Suas opçoes:\n[0] Pedra\n[1] Papel\n[2] Tesoura')
jogador = int(input('Qual é a sua Jogada?'))
if jogador == 0 or jogador == 1 or jogador == 2:
    from time import sleep
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!!')

    print(f'Maquina Escolheu: {maquina}')
    print(f'Jogador escolheu: {jogador}')

    print('-='*10)
    if jogador == maquina:
        print('Jogador Ganhou!!')
    else:
        print('Maquina Ganhou!!')
    print('-='*10)
else:
    print(f'{cores["vermelho"]}Opção de Jogada Inválida!{cores["limpa"]}')
