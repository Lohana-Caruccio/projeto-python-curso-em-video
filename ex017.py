from math import pow, sqrt
adj = float(input('Digite o valor do cateto adjacente de um triângulo: '))
opos = float(input('Digite o valor do cateto oposto: '))
quadradohi = pow(adj,2) + pow(opos,2)
hipotenusa = sqrt(quadradohi)
print('Dado o valor do cateto adjacente {:.2f} e do cateto oposto de {:.2f}.\n'
      'O comprimento da sua hipotenusa será {:.2f}.'.format(adj, opos, hipotenusa))