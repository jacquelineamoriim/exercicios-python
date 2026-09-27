frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A aparece pela primeira vez na posição {} da frase'.format(frase.find('A')+1))
print('A última ocorrência de A aparece na posição {} da frase'.format(frase.rfind('A')+1)) #+1 para contabilizar a partir do primeiro ao invés de zero.