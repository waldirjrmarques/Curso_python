'''
Refaça o deafio 035 dos triãngulos, acrescentando o recurso de mostrar que tipo de triãngulo será formado:
-Equilátero:todos os lados iguais
-Isósceles:dois lados iguais
-Esaleno:todos os lados diferentes
'''
cores = {'limpa':'\33[m',
         'azul':'\033[34m'}

print(f'{cores["azul"]}******************************{cores["limpa"]}')
print('      Verificar Triângulo   ')
print(f'{cores["azul"]}******************************{cores["limpa"]}')

l1 = float(input('Primeiro  segmento: '))
l2 = float(input('Segundo   segmento: '))
l3 = float(input('Terceiro  segmento: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Pode formar um triãngulo')
    if l1 == l2 == l3:
        print('Triângulo: Equilátero')
    elif l1 == l2 or l1 == l3 or l2 == l1 or l2 == l3:
        print('Triângulo: Isósceles')
    elif l1 != l2 != l3 != l1:
        print('Triângulo: Escaleno')
else:
    print('Não pode formar um Triãngulo')


