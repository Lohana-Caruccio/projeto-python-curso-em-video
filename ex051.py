#10 PRIMEIROS TERMOS DE UMA PA
print('='*50)
print('{: ^48}'.format('10 TERMOS DE UMA PA'))
print('='*50)
t1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = t1 + (11-1) * r
for c in range(t1,decimo, r):
    print('{}'.format(c), end=' -> ')
print('ACABOU')









