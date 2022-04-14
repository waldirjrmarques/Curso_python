#Crie um programa que leia quantos dinheiro uma pesoa tem na carteira e mostre quantos dólares ela pode comprar
real =  float(input('QUANTO VOCE TEM EM DINHEIRO R$: '))
dolar = 5.30
conversao = real / dolar

print('VOCÊ TEM R$:{} CONVERTIDO EM DOLAR VOCÊ TERIA USD:{:.2f}'.format(real,conversao))