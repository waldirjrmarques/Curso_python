'''
Fça um programa que jogue par ou impar com o computador . o JOGO só será interronpido quando o jogador perder, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

contador = 0
while True:
 print('=-'* 15)
 print('Vamos jogar Par ou Impar')
 print('=-'* 15)
 from random import randint
 maquina = randint(0,10)
 #print(maquina)
 jogador = int(input('Digite um valor: '))
 pi = str(input('Par ou Impar [P / I]')).strip().upper()[0]
 soma = maquina + jogador
 #print(soma)
 if soma % 2 == 0 and pi == 'P':
    contador += 1
    print(f'Você jogou {jogador} e o computador {maquina}. total: {soma} Par')
    print('Você Venceu!!')
 if soma % 2 != 0 and pi == 'P':
    print(f'Você jogou {jogador} e o computador {maquina}. total: {soma} Impar')
    print('Você perdeu!!')
    break
 if soma % 2 != 0 and pi == 'I':
  contador += 1
  print(f'Você jogou {jogador} e o computador {maquina}. total: {soma} Impar')
  print('Você Venceu!!')

 if  soma % 2 == 0 and pi == 'I':
  print(f'Você jogou {jogador} e o computador {maquina}. total: {soma} Par')
  print('Você perdeu!!')
  break

print('=-'* 15)
print(f'GAMER OVER! Você venceu {contador} vezes')







