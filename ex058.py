#Jogo da advinhação
from random import randint
from time import sleep
computador = randint(0,10)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print(' ')
cont = 0
acertou = False
while not acertou:
    jogador = int(input('Em que número pensei? '))
    cont += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos, tente novamente: ')
        elif jogador < computador:
            print('Mais, tente novamente: ')
print('...')
sleep(2)
print('ACERTOU!\nO número foi {} e você precisou de {} tentativas.'.format(computador, cont))
