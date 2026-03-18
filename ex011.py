lar = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
area = lar * alt
litrosnecessario = area/2
print('Considerando a largura e a altura da parede, sua área é de {}m\u00B2.\nE a quantidade de tinta necessária '
      'para pintá-la será de {}L.'.format(area,litrosnecessario))