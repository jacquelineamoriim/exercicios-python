#é importante colocar o tipo primitivo 'int' antes do input pra que tudo que o input receber seja inteiro
n1 = int(input ('Digite um número'))
n2 = int(input('Digite outro número'))
s = n1 +n2
print('A soma de {} e {} é {}'.format(n1, n2, s))
#pra que de fato ocorra a soma o temos que colocar o tipo primitivo int se não o sistema entende que é uma string então ele apenas junta os valores
