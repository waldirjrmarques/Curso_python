#criando uma função
def linha():
    print('-='*30)
#Mostrando a função criada
linha()


def mensagem(msg):
    print('-='*30)
    print(msg)
    print('-=' * 30)
mensagem(f'{"SISTEMA DE ALUNOS":^60}')
mensagem(f'{"CADASTRO DE ALUNO":^60}')
mensagem(f'{"TESTES":^60}')

def soma(a,b):
    print('-=' * 30)
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    print('-=' * 30)
soma(4, 5)
soma(8, 9)
soma(b=2, a=1) #declarando ordem dos valores
soma(a=5, b=5) #declarando ordem dos valores


#passando valores diferente COM TIPLA
def contador(*num):
    print('-=' * 30)
    for valor in num:
        print(f'{valor}',end= '  ')
    print()
    tam = len(num)
    print(f'recebi os valores {num} e são {tam} números')
    print('-=' * 30)
contador(1,6,4)
contador(5,6,4,7,7)
contador(1,0)

print('-=' * 30)

#trabalhando com lista
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
valores = [6, 1, 9, 4, 4]
dobra(valores)
print(valores)

#Desempacotamento Somando valores
def soma(* valores):
    print('-=' * 30)
    s=0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')
    print('-=' * 30)
soma(5, 6)
soma(4, 8, 9, 7 )

print('\n')

def quercontinuar():
    while True:
        resp = str(input('Quer continuar [S / N ] ')).strip().upper()[0]
        while resp != 'S' and resp != 'N':
            print('ERRO! Por Favor, digite apenas S ou N. ')
            resp = str(input('Quer continuar [S / N ] ')).strip().upper()[0]
        if resp == 'N':
            break

quercontinuar()

