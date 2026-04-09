#PA utilizando o while
print('Gerador - 10 TERMOS DE UMA PA - ')
print(' ')
t1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
print(' ')
termo = t1
cont = 1
while cont <= 10:
    print('{}'.format(termo), end='')
    print(', ' if cont < 10 else '.', end='')
    termo = termo + r
    cont = cont + 1
print(' ')
print('\nFIM!')
















