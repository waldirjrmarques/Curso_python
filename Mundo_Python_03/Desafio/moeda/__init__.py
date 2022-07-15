'''
ex:107
'''
def dobro(n):
    return f'{n * 2}'.replace('.',',')

def triplo(n):
    return f'{n * 3}'.replace('.',',')

def metade(n):
    return f'{n / 2}'.replace('.',',')

def aumentar(n,taxa):
    n = n + (n * (taxa / 100))
    return f'{n}'.replace('.',',')


def diminuir(n,taxa):
    n = n - (n * (taxa / 100))
    return f'{n}'.replace('.',',')
