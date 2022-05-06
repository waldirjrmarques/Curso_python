'''
ANSI - scape sequence
\033[style:text:back m
ex:\033[0;33;44m

# style
0 - none
1 - bold
4 - underline
7 - negative

# Text
30 - branco
31 - vermelho
32 - verde
33 - amarelo
34 - azul
35 - lilas
36 -  ciano
37 -  cinza

# Back
40 - branco
41 - vermelho
42 - verde
43 - amarelo
44 - azul
45 - lilas
46 -  ciano
47 -  cinza

'''
print('\033[0;30;41mTeste\033[m')
print('\033[4;33;44mTeste\033[m')
print('\033[1;35;43mTeste\033[m')
print('\033[30;42mTeste\033[m')
print('\033[mTeste\033[m')
print('\033[7;30mTeste\033[m')


# roots de cores
cores = {'limpa':'\33[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('-----------------------------')
print(f'Teste {cores["azul"]}AZUL{cores["limpa"]} teste')
print(f'Teste {cores["amarelo"]}AMARELO{cores["limpa"]} teste')
print(f'Teste {cores["pretoebranco"]}PRETO E BRANCO{cores["limpa"]} teste')


