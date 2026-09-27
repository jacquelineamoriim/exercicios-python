#calculando aluguel de carros
dias = int(input('Quantos dias alugados?: '))
km = float(input('Quantos km rodados?: '))
preco = (dias*60) + (km * 0.15)
print('O total a pagar é de {:.2f}'.format(preco))