'''
Modularização
 * Surgiu na decada de 60
 * Sistemas ficando cada vez maiores
 * Foco 01: Dividir um programa grande
 * foco 02: AUmentar a legibilidade
 * Foco 03: Facilitar a manutenção do sistema

 principal vantagem  da Modularização é dividir um problema grande em pequenos problemas

 VANTAGEM Modularização:
    * Organização do códico
    * Facilidade na manutenção
    * Ocultação de código detalhado
    * Reutilização em outros projetos

  como criar um pacote:
   01 -  botao direto do mouse  na pasta > new >python Package
'''


from uteis import numeros #chama o pacote que tem a função numeros
num = int(input('Digite um valor: '))
print(f'O Fatorial de {num} é {numeros.fatorial(num)}')
print(f'O DOBRO DE {num} é {numeros.dobro(num)}') #função dobro
print(f'O triplu DE {num} é {numeros.triplo(num)}') #funçao triplu