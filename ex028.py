from random import randint #gera o numero inteiro aleatório
from time import sleep #faz esperar alguns segundos
computador =  randint(0, 5) #faz o computador "PENSAR"
print('-=-' *20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' *20)
jogador = int(input('Em que número pensei? '))#jogador tenta adivinhar
print('PROCESSANDO ...')
sleep(2) #aqui eu coloco quanto tempo quero que espere
if jogador == computador:
    print('Parabéns você acertou!!')
else:
    print('Que pena! Você errou. Eu pensei no número {} e não no {}.'.format(computador, jogador))

