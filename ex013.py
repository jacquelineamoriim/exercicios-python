#calculando reajuste de salário
salario =float(input('Qua é o salário do funcionário? R$'))
aumento = salario + (salario * 15 / 100)
print('Um funcionário que ganhava {}, com 15% de aumento, passa a receber R${}'.format(salario, aumento))