'''
Crie um programa que tenha uma tupla totalmente preenchida com um contagem de zero ate vinte
Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostar-lo por extenso.
'''
numero = ('Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito',
            'Nove','Deis','Onze','Doze','Treze','Quatoze','Quinze','Dezesseis',
            'Dezessete','Dezoito','Dezenove ','Vinte')
while True:
    while True:
        posicao = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= posicao <= 20:
            break
        print('Posição Inválida:',end=' ')
    print(f'Você digitou o numero: {numero[posicao]}')
    validar = str(input('Quer Continuar [S / N]')).strip().upper()[0]
    if validar == 'N':
        break