from math import radians, sin, cos, tan
ang = float(input('Digite o valor de um ângulo: '))
sen = sin(radians(ang))
print('O ângulo {} tem o SENO de {:.2f}.'.format(ang,sen))
cos = cos(radians(ang))
print('O ângulo de {} tem o COS de {:.2f}.'.format(ang,cos))
tan = tan(radians(ang))
print('O ângulo de {} tem o TAN de {:.2f}.'.format(ang,tan))