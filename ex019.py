#Sorteando  um item da lista
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4] #criando uma lista de alunos
escolhido = random.choice([n1, n2, n3, n4]) #random choice escolhe um valor pra exibir
print('O aluno escolhido foi {}'.format(escolhido))