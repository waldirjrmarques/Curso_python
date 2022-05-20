'''
Crei um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
-Média abaixo de 5.0 : Reprovado
-Média entre 5.0 e 6.9: Recuperação
-Media 7.0 ou superior: Aprovado
'''
cores = {'limpa':'\33[m',
         'azul':'\033[34m'}

print(f'{cores["azul"]}******************************{cores["limpa"]}')
print('      Avaliação aluno   ')
print(f'{cores["azul"]}******************************{cores["limpa"]}')

nota01 = float(input('Informe sua primeira nota:'))
nota02 = float(input('Informe sua segunda nota:'))
media = (nota01 + nota02) / 2

if media < 5.0:
    print(F'Média:{media}, Aluno Reprovado!')
elif media >= 5.0 or media < 7:
    print(F'Média:{media}, Aluno Recuperação!')
elif media >= 7:
    print(F'Média:{media}, Aluno Aprovado!')