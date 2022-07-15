'''
Crie um mÓDULO chamado moeda.py que tenha as funçoes incorporadas aumentar(), dimiuir(),dobro() e metade().
Faça também um programa que importe esses módulos e use essas funções.
'''
import moeda

valor = float(input('Digite o preço: R$'))
print(f'A metade de R$:{mvalor} é R$:{moeda.metade(valor)}')
print(f'A dobro de R$:{valor} é R$:{moeda.dobro(valor)}')
taxa = int(input(f'R${valor}  com aumento de %:'))
print(f'Com aumento de {taxa}% R$:{valor} é R$:{moeda.aumentar(valor,taxa)}')
taxa = int(input(f'R${valor}  com desconto de %:'))
print(f'Com desconto de {taxa}% R$:{valor} é R$:{moeda.diminuir(valor,taxa)}')
