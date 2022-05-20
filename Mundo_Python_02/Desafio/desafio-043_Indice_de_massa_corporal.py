'''
Desenvolva uma logica que leia o peso e a altura de uma pessoa.
calcule seu IMC  e mostre seu status, de acordo com a tabela abaixo:
-Abaixo de 18.5: Abaixo do Peso
-Entre 18.5 e 25: Peso Ideal
-De 25 até 30: Sobrepeso
-De 30 até 40: Obesidade
-Acima de 40: Obesidade Mórbida
'''

peso = float(input('Informe seu Peso:'))
altura = float(input('Informe sua Altura:'))
imc = peso / (altura ** 2)


if imc < 18.5:
    print(f'IMC:{imc:.2f} Abaixo do Peso')
elif imc >= 18.5 and imc <= 25:
    print(f'IMC:{imc:.2f} Peso Ideal')
elif imc > 25 and imc <= 30:
    print(f'IMC:{imc:.2f} Sobrepeso')
elif imc > 30 and imc <= 40:
    print(f'IMC:{imc:.2f} Obesidade')
elif imc > 40:
    print(f'IMC:{imc:.2f} Obesidade Mórbida')


