from datetime import date
from time import sleep

atual = date.today().year
cont1 = 0
cont2 = 0
cont3 = 0
soma = 0
print('-'*55)
print('Desejam saber se já atingiram a maioridade?')
print('-'*55)
print('Responda a baixo')
sleep(1)
print(' ')
for c in range(1,8):
 ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
 cont1 += 1
 if atual - ano >= 21:
    cont2 += 1
 else:
    cont3 += 1
print(' ')
print('{: ^48}'.format('Dessas {} pessoas'.format(cont1)))
print('{} pessoas são maiores de idade'.format(cont2) )
print('{} pessoas são menores de idade'.format(cont3))
