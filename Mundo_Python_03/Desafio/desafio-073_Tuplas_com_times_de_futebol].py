'''
Crie um tupla preenchida com os 20 primeiros colocados da tabela do compeonato brasileiro de futebol,na ordem de colocaço,
Depois mostre.
* - Os 5 primeiros colocados.
* - Os últimos 4 colocados.
* - Times em ordem alfabética
* - Em que posição está o time do Paysandu
'''

times = ('Mirassol','Paysandu','ABC','Botafogo-PB','Remo','Figueirense','Volta Redonda','São José-RS','Manaus','Ypiranga-RS','Ferroviário',
         'Botafogo-SP','Vitória','Floresta','Aparecidense','Campinense','Confiança','Atlético-CE','Altos','Brasil de Pelotas',)
print(f'CLASSIFICAÇÃO SERIE C : {times}')
print('=-'* 15)
print(f'OS 5 PRIMEIROS COLOCADOS: {times[0:5]}')
print('=-'* 15)
print(f'OS 4 ULTIMOS COLOCADOS: {times[-4:]}')
print('=-'* 15)
print(f'TIME EM ORDEM ALFABÉTICA:{sorted(times)}')
print(f'O {times[1]} está na {times.index("Paysandu")+1}ª colocação do campeonato')

