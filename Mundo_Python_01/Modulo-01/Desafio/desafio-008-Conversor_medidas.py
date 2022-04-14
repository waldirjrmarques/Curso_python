#Escreva um programa em metros e o exiba convertido em centimetros e milimetros
metros = float(input('Informe quantos metros deseja converter: '))
centimetro = metros * 100
milimetro = metros  * 1000
print('{} metros equivale há {} centimetros.\n{} metros equivale há {} milimetros.'.format(metros,centimetro,metros,milimetro))