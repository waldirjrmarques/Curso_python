'''
Crie um programa que tenha a função leiaint() que vai funcionar de forma semelhante a função input() do python,
só que faznedo a validação para acaietar apenas um valor numerico.
ex: n = leaint('Digite um numero')
'''

def leiaInt(msg):
   fim = False
   while True:
        n = str(input(msg))
        if n.isnumeric(): #se for numero passa str para int
            n = int(n)
            fim = True
        else:
            print('ERRO! Digite um numero inteiro válido.')
        if fim:
            break
   return n

n = leiaInt('Digite um numero:')

#retorno da função
print(f'Você acabou de digitar o número {n}')

