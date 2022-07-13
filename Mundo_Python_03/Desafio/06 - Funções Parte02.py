'''
# Interactive help =  Ajuda Interativa
    help()
        Pesquisa o que cada comando faz, para pesquisar deve acessar o (python console) e digitar help(), após isso
        digite o comando a ser pesquisado,  para finalizar digite exit. pode tambem acessar o help diretamento ex: help(print)
'''
help(print)
print(input.__doc__)



''''
# Docstrings 
    Crie  uma documentação com das informaçoes da função criada , para criar uma documentação pasta abrir ''' ''' como o exemplo abaixo:,
    após isso basta chamar o help da funçao criada 
'''

def contador(i,f,p):
    '''
        -> faz a contagem e mostra na tela
        :param i: inicio da contagem
        :param f: fim da contagem
        :param p: passo da contagem
        :return: sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('Fim!')
contador(2,10,2)
help(contador)


'''
#Parâmetros opcionais
    def somar(a=0,b=0,c=0):
'''
def somar(a=0,b=0,c=0):
    soma = a+b+c
    print(f'A soma vale {soma}')

somar(3,2,5)
somar(8,4)
somar(a=5,b=2)
somar()


'''
#Escopo de variáveis
'''
#exemplo 01
def teste01():
    n = 5 # variavel n local com o mesmo nome da varial global mas com valores diferentes
    x = 8 #variavel interna
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa Principal
n = 2 #variavel n global
print(f'No programa principal, n vale {n}')

teste01()
'''print(f'No programa principal, x vale {x}')''' #erro , nao retono valor da varialvel local


#exemplo 02
print('-='* 30)
def teste02():
    global n #usa a variavel global
    n = 5 # variavel n global
    print(f'Na função teste02, n vale {n}')

# Programa Principal
n = 2 #variavel n global
print(f'No programa principal, n vale {n}')

teste02()
print(f'{n}') #usando a variavel global dentro da funçao internal e retor nando um novo valor da varialvel .



'''
# Retornos de valores
'''
def somar(a=0,b=0,c=0):
    soma = a+b+c
    return soma # Retornos de valores

r1 = somar(3,2,5)
r2 = somar(8,4)
r3 = somar(a=5,b=2)
r4 = somar()
print(f'Meus calculos fora {r1}, {r2}, {r3} e {r4}')

'''
Praticando
'''

def fatorial(num = 1):
    f = 1
    for c in range (num,0 , -1):
        f *= c
    return f

n = int(input('Digite um número:'))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}')


def par(n=0):
    if n % 2 ==0:
        return True
    else:
        return False

num = int(input('Digite um Número:'))
if par(num):
    print('É PAR!')
else:
    print('Não é par ')