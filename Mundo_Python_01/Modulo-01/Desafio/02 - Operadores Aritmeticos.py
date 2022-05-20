'''
Operadores Aritmeticos

Adição -> +
Subtração -> -
Multiplicação -> *
Divisão -> /
Potência -> **
Divisão Inteira -> //
Resto da Divisão -> %
'''
adicao = 5 + 2
print(adicao)

subtracao = 5 - 2
print(subtracao)

multiplicacao = 5 * 2
print(multiplicacao)

divisao = 5 / 2
print(divisao)

potencia = 5 ** 2
print(potencia)

div_int = 5 // 2
print(div_int)

res_div = 5 % 2
print(res_div)
'''
Ordem de precêdencia

1° -> ()
2° -> **
3° -> * , / , // , %
4° -> + , -
'''
resp01 = 5 + 3 * 2
print(resp01)

resp02 = 3 * 5 + 4 ** 2
print(resp02)

resp03 = 3 * (5 + 4 ) ** 2
print(resp03)


'''
Outras funções com operadores aritmeticos 
'''
teste01 = ('oi' + 'oi')
print(teste01)

teste02 = ('Oi' * 5)
print(teste02)

teste03 = ('=' * 20)
print(teste03)

# {:20} Coloca 20 caracteres depois da variavel
nome01 = input('Qual é su nome?')
print('Prazer em te conhecer {:20}!'.format(nome01))

#{:>20} Cololoca a varialvel com 20 caracteres alinhada a direita
nome02 = input('Qual é su nome?')
print('Prazer em te conhecer {:>20}!'.format(nome02))

# {:<20} Cololoca a varialvel com 20 caracteres alinhada a esquerda
nome03 = input('Qual é su nome?')
print('Prazer em te conhecer {:<20}!'.format(nome03))

# {:^20} Cololoca a varialvel com 20 caracteres centralizado
nome04 = input('Qual é su nome?')
print('Prazer em te conhecer {:^20}!'.format(nome04))


# {:=^20} Cololoca a varialvel com 20 caracteres centralizado com = ou qualquer caractere
nome05 = input('Qual é su nome?')
print('Prazer em te conhecer {:=^20}!'.format(nome05))

# {:.3f} Coloca casas decimas de acordo com o numero informado.
valor = int(input('Digite um valor?'))
print('{:.3f}'.format(valor))


#end= '' deixa os printes na mesma linha
#\n quebra linha do print
print ('Teste de print \n com python com guanabara', end= ' ')
print ('Outra parte de teste com print.')

'''
Tabela - Operadores Relacionais
==	Igual a
!=	Diferente
>=	Maior ou igual
>	Maior que
<	Menor que
<=	Menor ou igual
'''

'''
Operadores Lógicos
or	OU lógico
and	E lógico
not	Negação
'''

'''
Tabela de precedência em Python
- menos unário(sinal de número negativo)    Executado Antes
* / Operadores Multiplicativos
+ -    Operadores aditivos
< > <= >= == != Relacionais
not Operador de negação
and e lógico Executado Depois
or ou lógico 
'''
