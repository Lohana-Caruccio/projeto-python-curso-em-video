#Dividindo valores em várias listas
todosN = list()
numP = list()
numI = list ()
while True:
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if n not in todosN:
        todosN.append(n)
    if n % 2 == 0 and n not in numP:
        numP.append(n)
    else:
        if n % 2 == 1 and n not in numI:
            numI.append(n)
    if r in 'Nn':
        break
print('-='*30)
print(f'Lista com todos os valors{todosN}')
print(F'Lista com valores pares {numP}')
print(f'Lista com valores ímpares {numI}')