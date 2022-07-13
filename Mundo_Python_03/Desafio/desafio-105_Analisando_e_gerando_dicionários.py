'''
Faça um programa que tenha função notas() que pode receber várias notas de alunos e vai retornar um dicionario com as seguintes informações.

* Quantidade de notas
* A maior nota
* A menor nota
* a média da turma
*A situação (opcional)
obs: Adicione também as docstrings.
'''
def notas(*num,sit=False):
    '''
    -> FUNÇÃO para analisar a situação de vários alunos.
    :param num: uma ou mais notas dos alunos (aceitavarias
    :param sit: valor opcional, indicando se deve ou não adcionar a situação
    :return: dicionario com várias informaçoes sobre a situaçaão da turma.
    '''
    dicionario = dict()
    dicionario['total'] = len(num)
    dicionario['maior'] = max(num)
    dicionario['menor'] = min(num)
    dicionario['media'] = sum(num) / len(num)
    if sit:
        if dicionario['media'] >= 7.0:
            dicionario['situação'] = 'Boa'
        elif dicionario['media'] >= 5.0:
            dicionario['situação'] = 'Razoável'
        else:
            dicionario['situação'] = 'Ruim'

    return dicionario

n = notas(5.5, 2.5 ,1.5,sit=True)
print(n)

help(notas)