'''
Faça um mini-ststema que utilize o interactive help do python. O usuario vai digitar o comando e o comando e o manual
vai aparecer. Quando o usuario digitar a palavra 'FIM' , o programa se encerrará.
obs: use cores

'''
from time import sleep
c = ('\033[m',           # 0 - sem cor
       '\033[0;30;41m',  # 1 - vermelho
       '\033[0;30;42m',   # 2 - verde
       '\033[0;30;43m',   # 3 - amarelo
       '\033[0;30;44m',   # 4 - azul
       '\033[0;30;45m',  # 5 - roxo
       '\033[7;40m');    # 6 - branco


#02 Mostra menssagem
def ajuda(com):
    titulo(f'Acesando o manual do comando {com}',4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(0.3)

def titulo(msg,cor=0):
    tamanho = len(msg) + 4
    print(c[cor],end='')
    print('~' * tamanho)
    print(f"  {msg}")
    print('~' * tamanho)
    print(c[0], end='')
    sleep(0.3)


#01Programa principal
comando = ''
while True:
    titulo('Sistema de ajuda PyHELP',1)
    comando = (str(input('Comando ou biblioteca:')))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)