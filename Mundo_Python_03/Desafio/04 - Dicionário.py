'''
 Tupla inicia com ()
Lista inicia com []
Dicionario inicia com {}
'''
#criando dicionario
dados = dict()
dados = {'nome':'Pedro','idade':25}
print(dados)
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M' #adcionando um elemento no final do dicionario
print(dados)
del dados['idade'] #removendo idade
dados['nome'] = 'Leandro' # reatribuindo nome de pedro para leandro
print(dados)

print("-="*30)
filmes = {
    'titulo':'star wars',
    'ano':'1977',
    'diretor':'George Lucas'
}
print(filmes)
print(filmes.values()) #mostra os valores do dicionario
print(filmes.keys()) #mostra as chaves do dicionario
print(filmes.items()) #mostra cada informação separadamente
for chave ,valor in filmes.items():
    print(f'O {chave} é {valor}')
print("-="*30)
for valor in filmes.values():
    print(f'{valor}')
print("-="*30)
for chave in filmes.keys():
    print(f'{chave}')
print("-="*30)

#dicionario dentro de lista
locadora = [filmes,filmes]
print(locadora)
print(locadora[0]['ano'])

print("-="*30)

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(estado)
print(brasil)

for estado in brasil:
    for valor in estado.values():
        print(valor,  end='  ')
    print()


