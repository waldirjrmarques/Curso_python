'''
#Estrutura de repetição com variavel de controle.

for = laço
c = variavel de controle
in =  no
range = intervalo
(0,5) =  quantas vezes vai repetir

for c in range(1,5):
    print('oi')
'''
#Vai escrever oi 5x
for c in range(0,5):
    print('oi')
print('-----Fim-----')

# Vai contar de 1 a 5:
for c in range(0,5):
    print(c)
print('-----Fim-----')

# Vai contar de 5 até 1
for c in range(5,0,-1):
    print(c)
print('-----Fim-----')

#Vai contar de 0 até 5 con saldo de 2
for c in range (0,5,2):
    print(c)
print('-----Fim-----')

#Com entrada de dados
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
salto = int(input('Salto: '))
for c in range (inicio,fim,salto):
    print(c)

#Somando numero
s = 0
for c in range (0,3):
    n = int(input('Informe um numero: '))
    s = s + n
print(f'soma = {s}')