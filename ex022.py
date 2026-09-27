nome = str(input('Digite seu nome completo: ')).strip() # aqui solicita o nome ao usuário especificando o tipo string e usando strip para já tirar os espaços possíveis que ele pode incluir ao digitar atr
print('Analisando seu nome...') #escreve analisando seu nome na tela
print('Seu nome em maiúsculas é:{}'.format(nome.upper())) #aqui eu uso .format (nome upper pra deixar todas em maiusculo
print('Seu nome em minúsculas é: {}'.format(nome.lower())) #aqui eu uso .format(nome lower pra deixar todas em minusculo
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' '))) #aqui através do len(nome) ele conta qts letras tem o nome e subtrai os espaços através de nome.count('')
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split() # criamos uma variável que recebe os nomes divididos
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
#aqui no print format(separa[0] ele vai me mostrar o conteúdo da variável separa mostrando a posição zero pois começa sempre com zero. Nesse caso o primeiro nome.
# Depois ele mostra no len(separa[0] é pra saber quantas letras tem no primeiro nome.
