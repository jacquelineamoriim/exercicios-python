real = float(input('Quanto de dinheiro você tem na carteira? R$ '))
dolar = real / 5.42 #considerando o valor do dolar
print('Com R${} você pode comprar US${:.2f}'.format(real, dolar))