'''
Escreva um programa para aprovar o empréstimo bancario para a compra de uma casa.Pergunte o valor da casa, o salário do
comprador e em quantos anos ele vai pagar.
A prestação mensal, nao pode exceder 30% do salário  ou antão o empréstimo será negado.
'''
cores = {'limpa':'\33[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'pretoebranco':'\033[7;30m'}

print(f'{cores["azul"]}******************************{cores["limpa"]}')
print('Analise de Credito Imobiliário')
print(f'{cores["azul"]}******************************{cores["limpa"]}')

valor_casa = float(input('Qual o valor do imovel? '))
salario_comprador = float(input('Qual valor do seu  salário liquido? '))
anos_parcela = int(input('Quantos anos deseja parcelar: '))
mes = anos_parcela*12
parcelasimovel = valor_casa / mes
porcentagem_salario = salario_comprador * (30/100)

print(f'Para pagar uma casa de R$:{valor_casa:.2f} em {anos_parcela} anos ',end='')
print(f'a prestação será de R$:{parcelasimovel:.2f}')
if parcelasimovel > porcentagem_salario:
    print(f'{cores["vermelho"]}Seu FINACIAMENTO REPROVADO (Parcela > 30% do salário {cores["limpa"]}')
else:
    print(f'{cores["azul"]}Seu FINACIAMENTO FOI APROVADO{cores["limpa"]}')
