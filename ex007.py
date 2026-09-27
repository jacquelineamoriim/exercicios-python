n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1+n2)/2 #ordem de precedência pra ser calculada, primeiro o parenteses.
print('A média entre {} e {} é igual a {:.2}'.format(n1, n2, m))