distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distancia))
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print('E o preço da sua viagem será de {:.2f}'.format(valor))
