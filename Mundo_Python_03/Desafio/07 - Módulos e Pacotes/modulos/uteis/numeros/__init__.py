def fatorial(n):
    f = 1
    for c in range(1,n+1):
        f *= c
    return f
def dobro(n):
    return n * 2

def triplo(n):
    return n * 3

def metade(n):
    return n / 2

def dezporcento(n):
    n = n +(n*(10/100))
    return n