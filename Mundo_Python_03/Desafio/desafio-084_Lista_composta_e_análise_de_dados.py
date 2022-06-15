'''

'''
galera = list()
dados = list()
numeros = list()
maiorlista = list()
nomesmaior = list()
menorLista = list()
nomesmenor = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    galera.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar [S / N ] ')).strip().upper()[0]
    while resp != 'S' and resp != 'N':
        print('ERRO')
        resp = str(input('Quer continuar [S / N ] ')).strip().upper()[0]
    if resp == 'N':
        break

#numeros = list()
for indice, valor in enumerate(galera):
    numeros.append(valor[1])
#Maior e Menor valor
maior = max(numeros)
menor = min(numeros)

#maiorlista / menorLista
for indice, valor in enumerate(galera):
    if maior in valor:
        maiorlista.append(valor)
    if menor in valor:
        menorLista.append(valor)

#nomesmaior = list
for indice, valor in enumerate(maiorlista):
    nomesmaior.append(valor[0])

#nomesmenor = list
for indice, valor in enumerate(menorLista):
    nomesmenor.append(valor[0])

print(f'Ao todo, você cadastrou  {len(galera)} pessoas.')
print(f'O maior peso foi {maior:.1f}Kg. Peso de {nomesmaior}')
print(f'O maior peso foi {menor:.1f}Kg. Peso de {nomesmenor}')
