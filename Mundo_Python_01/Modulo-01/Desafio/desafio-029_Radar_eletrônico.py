'''
Escreva um programa que leia a velociadede de um carro.
    Se ele ultrapassar 80km/h. mostre uma mensaggem dizendo que ele foi multado.
    A multa vai custar R$7.00 POR CADA KM acima do limite.
'''

km = float(input('Informe a valecidade do carro:'))

if km > 80:
    print(f'Você ultrapassou a velociade permitida de 80km/h. MULTADO EM R$:{(km - 80)*7}')
else:
    print('Parabéns você está no limite da velocidade.')