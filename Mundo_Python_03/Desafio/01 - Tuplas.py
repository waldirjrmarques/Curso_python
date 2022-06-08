'''
#Variaveis compostas
Conceito de Tuplas:
    O que é tupla? Tupla é um tipo de estrutura de dados utilizada em Python que funciona de modo semelhante a uma lista,
    entretanto, com a característica principal de ser imutável. Isso significa que quando uma tupla é criada não é possível
    adicionar, alterar ou remover seus elementos.

Tupla inicia com ()
Lista inicia com []
Dicionario inicia com {}

obs:Uma tupla em python aceita string e numeros
'''

#ex

lanche = ('Hamburguer','Suco','Pizza','Pudin')
#trabalhando com fatiamento
print(len(lanche))
print(lanche[1])
print(lanche[-2])
print(lanche[-1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])
print(lanche.index('Suco'))

#modo 1 sem posição
for comida in lanche:
    print(f'Eu vou comer -> {comida}')
#modo 2 com posição
for cont in range (0,len(lanche)):
    print(lanche[cont])
#modo 3 com posição
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

#Mostrar em ordem alfabética
print((sorted(lanche)))

#juntar tupla
a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c)
#quantas vezes o numero 5  aparece
print(c.count(5))
#mostra a posição 8
print(c.index(8))


d = b + a
print(d)

pessoas  = ('Gustavo',39,'M',99.88)
#del(pessoas) -> apaga atupla
print(pessoas)