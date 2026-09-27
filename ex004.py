a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
#vai mostrar que é uma string mesmo que coloque número pois não tem int
print('Só tem espaços', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanúmerico?', a.isalnum())
print('Está em letra maiúscula?', a.isupper())
print('Está em letra minúscula?', a.islower())
print('Está capitalizada?', a.istitle())
#o a nesse caso é um objeto