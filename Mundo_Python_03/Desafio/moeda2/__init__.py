'''
ex:108
'''
def dobro(n=0):
    return n * 2

def triplo(n=0):
    return n * 3

def metade(n=0):
    return n / 2

def aumentar(n=0,taxa=0):
    n = n + (n * (taxa / 100))
    return n


def diminuir(n=0,taxa=0):
    n = n - (n * (taxa / 100))
    return n

def moeda(preço=0,moeda='RS:'):
    return f'{moeda}{preço:4.2f}'.replace('.',',')


