#seno cosseno e tangente
import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo)) #converti para radiano o ângulo digitado para calcular o seno
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo de {} tem o consseno de {:.2f}'.format(ângulo, cosseno))
tan = math.tan(math.radians(ângulo))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ângulo, tan))
# caso queira importar somente  o sin, cos, tan e radians,colocaria import math  e esses respectivos e pode apagar os math que está no programa pois já irá importar todos os que mencionei