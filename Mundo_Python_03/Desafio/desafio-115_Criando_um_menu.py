'''
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em uma arquivo de texto simples.
O sistema SÓ vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastrada.
'''

from desafio115.lib.interface import *
from desafio115.lib.arquivo import *
from time import sleep

arq =  'Corso em video.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar novas Pessoas','Sair do Sistema'])
    if resposta == 1 :
        #opção de listar o conteúdo do arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...A té logo')
        break
    else:
        print('ERRO! Digite uma opção válida!')
    sleep(2)

