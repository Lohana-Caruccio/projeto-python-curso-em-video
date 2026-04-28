#Matriz com análise de dados
print('-=' * 30)
print(f'{"\033[1;36mCRIANDO UMA MATRIZ 3x3\033[m":^67}')
print('-=' * 30)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaP = soma3 = cont = maiorV = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            somaP += matriz[l][c]
print(' ')
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end = ' ')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {somaP}.')
for l in range(0,3):
    soma3 += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {soma3}.')
for c in range(0,3):
    if c == 0 or matriz[1][c] > maiorV:
        maiorV += matriz[1][c]
print(f'O maior valor da segunda linha é {maiorV}.')

