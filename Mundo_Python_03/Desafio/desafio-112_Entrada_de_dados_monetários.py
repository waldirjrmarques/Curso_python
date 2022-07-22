'''
Dentro do pacote moeda4 que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiadinheiro()
que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.
'''

from moeda4 import resumo,leiadinheiro

p = leiadinheiro('Digite o preço: R$ ')

resumo(p,10,15)