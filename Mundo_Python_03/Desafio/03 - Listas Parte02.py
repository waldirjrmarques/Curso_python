'''

'''
#Lista dentro de outra lista
pessoas = [['Pedro',25],['Maria',19],['joao',32]]
print(pessoas)                #Mostra a lista
print(pessoas[0])             #Mostra a lista 0
print(pessoas[0][0])          #Mostra o indice 0 da lista 0

print(pessoas)                #Mostra a lista
print(pessoas[1])             #Mostra a lista 1
print(pessoas[1][0])          #Mostra o indice 0 da lista 1

#Mostra o nome e a idade de cada lista
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade')
print('-=' * 20)

#Criando lista multiplas com for
galera = list()
dados = list()
contmaior = 0
contmenor = 0
for c in range(0,3): #faz loop 3x
    dados.append(str(input('Nome: ')))      #adiciona a nome na lista dados
    dados.append(int(input('Idade: ')))     #adiciona a idade na lista dados
    galera.append(dados[:])                 #faz uma copia[:] da lista dados e adiciona na lista galera
    dados.clear()                           #limpa a lista dados
print(galera)
#Verifica maiores e menores de idade dentro da lista
for p in galera:
    if p[1] >= 21:
        contmaior += 1
        print(f'O {p[0]} é maior de idade ')
    else:
        print(f'O {p[0]} é menor de idade ')
        contmenor += 1
print(f'Total maiores de idade: {contmaior}')
print(f'Total menores de idade: {contmenor}')
print('-=' * 20)