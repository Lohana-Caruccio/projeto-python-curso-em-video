#Extraindo dados de uma Lista
num = list()
c = c5 = rE = 0
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        c += 1
    else:
        print('Valor repetido, tente outro...')
    if n == 5:
        c5 += 1
    r = str(input('Quer continuar? [S/N] '))
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break
print('-='*30)
print(f'Foram digitados, sem contar os repetidos, {c} elementos!')
print(f'São eles em ordem decrescente:\n{sorted(num, reverse=True)}')
print(' ')
if c5 == 0:
    print('O valor 5 não foi digitado e não está na lista!')
else:
    print('O valor 5 foi digitado e está na lista!')


