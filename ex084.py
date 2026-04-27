#Lista Composta e Análise de dados
maiorpeso = menorpeso = 0
lista1 = list()
lista2 = list()
maisP = list()
menosP = list()
while True:
    lista1.append(str(input('Nome: ')))
    lista1.append(float(input('Peso: ')))
    if len(lista2) == 0:
        maiorpeso = menorpeso = lista1[1]
    else:
        if lista1[1] > maiorpeso:
            maiorpeso = lista1[1]
        if lista1[1] < menorpeso:
            menorpeso = lista1[1]
    lista2.append(lista1[:])
    lista1.clear()
    r = ' '
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break
for p in lista2:
    if p[1] <= 70:
        menosP.append(p[0])
    elif p[1] >= 100:
        maisP.append(p[0])
print('-='*30)
print(f'Foram cadastradas {len(lista2)} pessoas')
print(f'O maior peso foi de {maiorpeso:.1f}kg. E os mais pesados da lista foram: ', end='')
for i, p in enumerate(maisP):
    if i < len(maisP)-1:
        print(f'{p}', end=', ')
    else:
        print(f'{p}.')
print(f'O menor peso foi {menorpeso:.1f}kg. E os mais leves da lista foram: ', end = '')
for i, p in enumerate(menosP):
    if i < len(menosP)-1:
        print(f'{p}', end=', ')
    else:
        print(f'{p}.')
