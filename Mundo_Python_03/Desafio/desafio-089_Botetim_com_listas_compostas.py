'''

'''
turma = list()
aluno = list()
medias = list()

#Lococando nome e nota dos alunos na lista turma
while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    turma.append(aluno[:])
    aluno.clear()
    resp = str(input('Quer continuar [S / N ] ')).strip().upper()[0]
    while resp != 'S' and resp != 'N':
        print('ERRO')
        resp = str(input('Quer continuar [S / N ] ')).strip().upper()[0]
    if resp == 'N':
        break

print('-='* 30)
print(f'{"No":<4}{"Nome":<10} {"Media":>8}')
print('-'* 30)

#escrevendo o indice, numee media de cada aluno
for indice, valor in enumerate(turma):
    media = (valor[1] + valor[2])/2
    medias.append(media)
    print(f'{indice:<4}',end='')
    print(f'{valor[0]:<10}',end='')
    print(f'{media:>8.1f}',end=' ')
    print()

#colocando  as notas de cada aluno na tela
while True:
    nota = int(input('Quer mostrar a nota de qual aluno?'))
    for indice, valor in enumerate(turma):
        if nota == indice:
            print(f'Nota de {valor[0]} {valor[1:]}')
    if nota == 999:
        print('Finalisando....')
        break

