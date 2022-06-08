'''

'''
print('--'* 15)
print('Lojas Super Baratão')
print('--'* 15)

totalcompra = 0
maior1000 = 0
menorpreco = 0
cont = 0
while True:
    cont += 1
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço do Produto: '))
    #total comprado
    totalcompra += preco
    #Produto maior de R$:1000,00
    if preco > 1000:
        maior1000 += 1
    #produto mais barato
    if cont == 1:
        menorpreco = preco
        menorproduto = produto
    else:
        if preco < menorpreco:
            menorpreco = preco
            menorproduto = produto
    stop = str(input('Quer continuar? [S / N]')).strip().upper()[0]
    if stop == 'N':
        break
print('---Fim do programa---')
print(f'O total de compra foi R$:{totalcompra:.2f}')
print(f'Temos {maior1000} produto custando mais que R$:1000,00')
print(f'O produto mais barato foi {menorproduto} que custa R${menorpreco:.2f}')