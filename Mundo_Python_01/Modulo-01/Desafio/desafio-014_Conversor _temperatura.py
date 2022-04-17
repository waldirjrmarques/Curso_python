'''
Escreva um programa que converta uma temperatura digitada em F° e converta em C°.
'''
Fahrenheit = float(input('Qual a temperatura em F°? '))
Celsius = (Fahrenheit - 32) / 1.8
print('A temperatura em {}F° corresponde a {}C°.'.format(Fahrenheit,Celsius))