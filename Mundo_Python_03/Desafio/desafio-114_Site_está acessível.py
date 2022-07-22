'''
Crie um código em python que teste se o site etsá acessivel pelo computador.
'''

import urllib.request

try:
    site = urllib.request.urlopen('https://email.sefa.pa.gov.br')
except:
    print('ERRO! Site não está acessível!')
else:
    print('Site está acessível!')
