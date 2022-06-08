'''
while Infinito
Usando o break para parar o loop infinito
'''
n = 0
s = 0
while True:
    n = int( input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')