'''
Faça u  programa qualquer e mostre se o ano é BISSEXTO
'''
from datetime import date
ano = int(input('Digite o ano para saber de é BISSEXTO: '))
if ano == 0:
    ano = date.today().year # pega o ano atual conf. maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(F'{ano} É ANO BISSEXTO')
else:
    print(F'{ano} NAÕ É ANO BISSEXTO')



