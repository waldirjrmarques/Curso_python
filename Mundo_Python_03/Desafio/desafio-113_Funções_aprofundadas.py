'''
Reescreva a fumção leiaInt()que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um númerode tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''

def leiaInt (msg):
   while True:
        try:
            n = int(input(msg))
        except(ValueError,TypeError):
            print(f'\033[31mERRO: Por favor , digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n
def leiafloat (msg):
   while True:
        try:
            n = float(input(msg))
        except(ValueError,TypeError):
            print(f'\033[31mERRO: Por favor , digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\n\033[31mUsuário preferiu não digitar esse número.\033[m')
        else:
            return n

n1 = leiaInt('Digite numero inteiro:')
n2 = leiafloat('Digite numero real :')

#retorno da função
print(f'Você acabou de digitar o numero inteiro {n1}')
print(f'Você acabou de digitar o numero real {n2}')
