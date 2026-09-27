#Conversor de temparatura
c = float(input('Informe a temperatura em °C: '))
f = 9*c/5+32 #não precisa de parenteses porque a ordem de precência de multiplicação e divisão são as mesmas.
print('A temperatura de {}:C corresponde a {}°F!'.format(c, f))