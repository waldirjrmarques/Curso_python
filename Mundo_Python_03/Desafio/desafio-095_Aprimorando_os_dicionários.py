'''

'''
jogador = dict()
lista = list()
gols = []
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0,partidas):
        gol = int(input(f'  Quantos gols na {c+1}° partida? '))
        gols.append(gol)
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    lista.append(jogador.copy())
    gols.clear()
    resp = str(input('Quer continuar [S / N ] ')).strip().upper()[0]
    while resp != 'S' and resp != 'N':
        print('ERRO! Por Favor, digite apenas S ou N. ')
        resp = str(input('Quer continuar [S / N ] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*30)
print(lista)
print('-='*30)

print('-='* 30)
print(f'{"Cod":<4}{"Nome":<4}{"Gols":>10} {"Total":>8}')
print('-'* 30)
for indice, valor in enumerate(lista):
    print(f'{indice:<4}',end='')
    print(f'{valor["nome"]:<4}',end='')
    print(f' {valor["gols"]}',end='')
    print(f'{valor["total"]:>8.1f}',end='')
    print()
print('-='* 30)

while True:
    resp = int(input('Quer mostrar os dados de qual jogador?(999 para)'))
    if resp >= len(lista):
        print(f'ERRO! Não existe jogador com código {resp}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {lista[resp]["nome"]}:')
        for jogo, gol in enumerate(lista[resp]["gols"]):
            print(f'  No jogo {jogo+1}  fez {gol} gols.')
    if resp == 999:
        break
    print('-=' * 30)



