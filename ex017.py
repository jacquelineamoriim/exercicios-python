#Catetos e Hipotenuza
#se quiser posso mudar pra from math hypot e apagar o math da sexta linha
from math import hypot
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimeiro do Cateto Adjascente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
