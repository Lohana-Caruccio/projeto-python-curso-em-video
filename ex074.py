#Maior e menor valor em uma tupla
from random import randint
valores = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
cont = 0
for v in valores:
    print(f'{v}', end=' ')
print(' ')
print(f'\nO maior valor sorteado foi {max(valores)}!')
print(f'O menor valor sorteado foi {min(valores)}!')