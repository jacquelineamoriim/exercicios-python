#sorteando uma ordem na lista
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4] #aqui eu crio a lista
random.shuffle(lista)# uso o shuffle para embaralhar a lista
print('A ordem de apresentação será ')
print(lista)
# se eu quiser importar apenas a biblioteca shuffle, lá em cima eu coloco from random import shffle
# e apago o random ali do meio do programa, deixo só a biblioteca que no caso é shuffle