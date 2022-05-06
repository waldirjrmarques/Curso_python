'''Manipulando texto - Fatiamento'''

#Mostrando só um indice da string [0]
teste = input('Escreva algo:')
print(teste[0])
#Mostrando o ultom indice da string[-1]
print(teste[-1])

#Mostrando um intervalo de indice da string ex: [9:13] (9 ate 13 excluindo o indice 13)
print(teste[9:13])

#Mostrando um intervalo de indice da string com salto  ex:[9:21:2] (motras o intervalo de 9 a 21 excluindo 21 com saldo de 2 em 2 do indice)
print(teste[9:21:2])

#Mostrando um intervalo de indice da string ex; [:5] (:5 sem informar o indice faz comecar do indice zero ate o 5)
print(teste[:5])

#Mostrando um intervalo de indice da string ex;[15:] (indice 15 ate o umtimo indice :)
print(teste[15:])

##Mostrando um intervalo de indice da string com salto  ex:[9::2] (motras o intervalo de 9  ate umtimo indice com saldo de 3 em 3 do indice)
print(teste[9::3])

''' Manipulando texto - Análise'''

# Função len verifica quantos caracteres tem a variavel.
print(len(teste))

# Função ex  teste.cont('0') verifica quantos o tem a variavel.
print(teste.count('o'))

# Função ex  teste.cont('o',0,13) verifica quantos o tem a variavel com fatiamento do indice 0 ate 13 excluindo 13.
print(teste.count('o',0,13))

#Função vericar em se tem  indice com nome 'a' e se tiver qual posição primeira. ex  teste.find('a')
print(teste.find('a'))

#Função vericar em se tem  indice com nome 'a' e se tiver qual a ultima posoção. ex  teste.find('a')
print(teste.rfind('a'))

#Função vericar em se tem  indice com 'android', se nao tiver retorna -1
print(teste.find('android'))

#função verifica se tem o nome 'Curso na frase' retorna verdadeiro ou falso
print('Curso'in teste)

''' Manipulando texto - Tranformação'''

# Função trocar uma frase ou paLavra ou outra
print(teste.replace('Python','android'))

# Função tranforma as letras minusculas em maiusculo.
print(teste.upper())

# Função tranforma as letras maiusculoas em minusculas.
print(teste.lower())

# Função tranforma todos os caracteres em minusculos  exeto a primeira letra.
print(teste.capitalize())

# Função  verifica quantras palavras tem e colocas elas com a primeira letra em maiusculo.
print(teste.title())

# Função remove espaços vazios do inicio e fim de uma string
#ex:   Aprenda Python
print(teste.strip())

# Função remove espaços vazios da direita da string
#ex:   Aprenda Python
print(teste.rstrip())

# Função remove espaços vazios da esquerda da string
#ex:   Aprenda Python
print(teste.lstrip())

'''Manipulando texto - Divisão de string'''

# Função divide a string e cada palavrae cada letra recebe novos indeces  cada palavra  recebe novos indice
print(teste.split())

#função junta as palavras colocando um string qualquer
print('-'.join(teste.split()))

#Imprimir testo inteiro
print('''
Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure beatae vero ullam eaque quas ea molestiae voluptate, 
eum neque consectetur perspiciatis explicabo aut saepe placeat! Ad nulla totam voluptates quae?
''')



