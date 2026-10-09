salario = float(input('Qual o salário do funcionário? R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava {:.2f} agora passa a ganhar {}'.format(salario, novo))
