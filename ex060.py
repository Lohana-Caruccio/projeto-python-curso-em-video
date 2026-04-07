#Cálculo de fatorial
n = int(input('Digite um número para calcular seu fatorial: '))
cont = n
fatorial = 1
print('Calculando {}! ='.format(n), end=' ')
while cont > 0:
    print('{} '.format(cont), end='')
    print('x ' if cont > 1 else '=', end='')
    fatorial = fatorial * cont
    cont = cont - 1
print(' {}'.format(fatorial))

