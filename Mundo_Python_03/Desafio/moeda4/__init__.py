'''
ex:110,111,112
'''
def dobro(n=0):
    n = n * 2
    return moeda(n)

def triplo(n=0):
    n = n * 3
    return moeda(n)

def metade(n=0):
    n = n / 2
    return moeda(n)

def aumentar(n=0,taxa=0):
    n = n + (n * (taxa / 100))
    return moeda(n)


def diminuir(n=0,taxa=0):
    n = n - (n * (taxa / 100))
    return moeda(n)

def moeda(preço=0,moeda='R$:'):
    return f'{moeda}{preço:4.2f}'.replace('.',',')

def resumo(preco,taxa_a=10, taxa_r=5):
    print('-'* 30)
    print('Resumo do valor'.center(30))
    print('-' * 30)
    print(f'Preço Analisado: \t{moeda(preco)}')
    print(f'Dobro do preço   \t{dobro(preco)}')
    print(f'Metade do preço  \t{metade(preco)}')
    print(f'Com {taxa_a}% de aumento \t{aumentar(preco,taxa_a)}')
    print(f'Com {taxa_r}% de redução \t{diminuir(preco,taxa_r)}')


def leiadinheiro(msg):
    valido =False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO! \"{entrada}\" é preço inválido\033[m')
        else:
            valido = True
            return float(entrada)



