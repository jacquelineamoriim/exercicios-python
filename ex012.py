#Calculando descontos
preco = int(input('Qual o preço do produto? R$ '))
valor = preco -(preco * 5/ 100)# calcula a porcentagem
valor2 = preco + (preco * 5/100)
print('O produto que custava {}, na promoção com o desconto de 5% vai custar R$ {}.'.format(preco, valor))
print(' O produto com 5% a mais seria {}'.format(valor2))