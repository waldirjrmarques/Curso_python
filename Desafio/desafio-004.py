# Faça um programa que leia algo pelo teclado e mostre na tela as informaçoes possiveis sobre ela.
n = input('Digite algo:')

#Comando mostra o tipo primitivo da varialvel
print('O tipo primitivo é ',type(n))

print('N é um número?',n.isalnum())
print('N é numérico?', n.isnumeric())
print('N é decimal?', n.isdecimal())
print('N é alfanumérico?', n.isalnum())
print('N é alfabético?', n.isalpha())
print('N é um dígito?', n.isdigit())
print('N está capitalizada?', n.istitle())
print('N é identificador?', n.isidentifier())
print('N está em caixa baixa?', n.islower())
print('N está em caixa alta?', n.isupper())
print('N é imprimível?', n.isprintable())
print('N é um espaço?', n.isspace())

