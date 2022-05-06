'''
Condição Simples

if = se
else = senao
'''

tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('Carro Novo')
else:
    print('Carro Velho')
print('---Fim---')


#Usando Condição Simplificada.

tempo = int(input('Quantos anos tem seu carro?'))
print('Carro Novo' if tempo<=3 else'Carro Velho')
print('---Fim---')

#--------------------------------

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2) / 2
print(f'A sua media foi {m:.1f}')
if m>=6.0:
    print('Sua média foi boa! . PARABENS!')
else:
   print('Sua média foi ruim! ESTUDE MAIS!')



