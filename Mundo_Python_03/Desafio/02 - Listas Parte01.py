'''
São arranjos seqüenciais de informações mais simplesCaracterizam­se por permitir o acesso eficiente
aos seus elementos em ordem seqüencialA definição clássica de uma lista como estrutura de dados abstrata
 compreende:
 Operação de construção de uma lista vazia
 Operação que testa se uma dada lista é vazia
 Operação para obter o primeiro elemento de uma lista
 Uma operação para adicionar um novo elemento no início de uma lista
 Operação para retirar o elemento inicial de uma lista

 Tupla inicia com ()
Lista inicia com []
Dicionario inicia com {}

OBS: A lista saão multaveis ou seja podem ser alteradas.
'''

lanche = [6 ,2 ,3 ,5 ]
print(lanche)
print('--'* 15)

lanche[0] = 8 #troca valor do indice 0 de 6 para 8
print(lanche)
print('--'* 15)

lanche.append(10) #Cria um novo indice na ultima posiçao com ex: o valor (10)
print(lanche)
print('--'* 15)

lanche.append('teste') #Cria um novo indice na ultima posiçao com ex: o valor ('teste')
print(lanche)
print('--'* 15)

lanche.insert(0,'inicio') #adciona um indice em qualquer posição da lista
print(lanche)
print('--'* 15)

lanche.insert(4,45) #adciona um indice em qualquer posição da lista
print(lanche)
print('--'* 15)

del lanche[5] #remove o indice 5 da lista
print(lanche)
print('--'* 15)

lanche.pop() #remove o ultimo indice da lista
print(lanche)
print('--'* 15)

lanche.pop(2) #Remove o indice 2 da lista
print(lanche)
print('--'* 15)

lanche.remove(3) #remove o valor 8 da lista
print(lanche)
print('--'* 15)

lanche.remove('inicio') #remove a palavra 'inicio' da lista
print(lanche)
print('--'* 15)

if 10 in lanche: # se tiver numero 10 na lista
    lanche.remove(10) #comanda para remover o numero 10
print(lanche)
print('--'* 15)

valores1 = list(range(1,11)) #criar um lista com range
print(valores1)
print('--'* 15)

valores2 = list(range(1,11,3)) #criar um lista com range com salto
print(valores2)
print('--'* 15)

valores3 = [5,8,4,9,3,1,4,5,]
print(valores3)
valores3.sort() # coloca a lista em ordem
print(valores3)
print('--'* 15)

valores4 = ['e','u','a','o']
print(valores4)
valores4.sort() # coloca a lista em ordem
print(valores4)
print('--'* 15)

valores4.sort(reverse=True) #embaralha o que estva em ordem
print(valores4)
print('--'* 15)

print(len(valores4)) #verificar o tamanho da lista
print('--'* 15)

#coloca os valores da linta com repetição
valores5 = [] #lista começando sem valores
valores5.append(2)
valores5.append(6)
valores5.append(8)
for v in valores5:
    print(f'{v}..',end='')
print('\n')
print('--'* 15)

#encontra o indice e o valor da lista
for indice, valor in enumerate(valores5):
    print(f'No indice {indice} encontrei o valor {valor}')
print('--'* 15)

#colocando valores em uma lista com repetição e range
valores6 = list()
for c in range(0, 5):
    valores6.append(int(input('Digite um valor:')))
print(valores6)
# mostrar o valor e o indice da lista
for ind, valorr in enumerate(valores6):
    print(f'No indice {ind} encontrei o valor {valorr}')
print('--'* 15)

#ligação entre lista( muda os valores das listas ligadas)
a = [2, 3, 5, 7, 9 ]
b = a
b[2] = 8
print(f'Lista A:{a}')
print(f'Lista B:{b}')
print('--'* 15)


#copia entre lista( Nao muda a lista a)
c = [2, 3, 5, 7, 9 ]
d = c[:] #copia dos valoes c em d
d[2] = 8
print(f'Lista A:{c}')
print(f'Lista B:{d}')
print('--'* 15)









