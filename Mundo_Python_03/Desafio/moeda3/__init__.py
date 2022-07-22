'''
ex:109
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

def moeda(preço=0,moeda='RS:'):
    return f'{moeda}{preço:4.2f}'.replace('.',',')


