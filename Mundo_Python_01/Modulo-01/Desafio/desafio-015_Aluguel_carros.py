'''
  Escreva
um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar,
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''
kmpercorrido = float(input('Quantos Km foram percorridos: '))
qdias = int(input('Quantos dias o carro foi alugado:'))

v_dia = 60
v_km = 0.15

total_km = kmpercorrido * v_km
total_dia = qdias * v_dia
total = total_km + total_dia

print('Você deve pagar R$:{:.2f} por {} percorrido'.format(total_km,kmpercorrido))
print('Você deve pagar R$:{:.2f} por {} dias alugado'.format(total_dia,qdias))
print('Total a pagar R$:{:.2f}'.format(total))