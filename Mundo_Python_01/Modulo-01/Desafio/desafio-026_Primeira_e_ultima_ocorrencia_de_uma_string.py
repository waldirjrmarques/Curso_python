'''
Faça um programa que leia uma frase pelo teclado e mostre:
 * Quantas vezes aparece a letra 'a'.
 * Em que posição ela aparece a primiera vez.
 * Em que posição ela aparece a ultima vez.
'''

frase = str(input('Escreva a frase: '))


print(f'A letra letra "A" apareceu {frase.strip().lower().count("a")}x')
print(f'A primeira letra "A" aparece na posição {frase.strip().lower().find("a")}')
print(f'A primeira letra "A" aparece na posição {frase.strip().lower().rfind("a")}')






