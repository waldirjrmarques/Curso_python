'''

'''

print('-'*40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-'*40)
listagem = ('Lapis',1.75,
            'Boracha',2.00,
            'Caderno',15.00,
            'Estojo',25.00,
            'Transferidor',4.75,
            'Compasso',9.75,
            'Mochila',100.75,
            'Canetas',22.75,
            'Livros',34.75,)
print(listagem)
for c in range(0,len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<30}',end='')
    else:
        print(f'R${listagem[c]:>7.2f}')
