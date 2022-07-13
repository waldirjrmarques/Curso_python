'''
Crie um programa que tenha uma função fatoria() que receba dois parametros: O primeiro que indique o numero a calcular  o outro chamado show, que será
um valor Lógico (opcional) indicando se será mostrado ou não na tela o processo de Calculo do fatorial
'''


#show=False FAZ SER OPCIONAL PARA MOSTRAR O RESULTADO
def fatorial(numero,show=False):
    '''
      --> Calcula o Fatorial de um número.
      :param numero: numero: O númeroa ser calculado.
      :param show: (opcional) Mostrar ou nao a conta
      :return: O valor do Fatorial de numero
    '''
    f = 1
    for c in range(numero, 0, -1):
        f *= c
        # show=False FAZ SER OPCIONAL PARA MOSTRAR O RESULTADO
        if show:
            print(c,end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return (f)



numero = int(input('Calcular seu Fatorial: '))
print(fatorial(numero)) #mOSTRANDO SO O RESULTADO
print(fatorial(numero,show=True)) #mOSTRANDO CALCULO COM RESOLTADO
help(fatorial)
