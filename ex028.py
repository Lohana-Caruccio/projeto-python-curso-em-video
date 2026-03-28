from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador pensar em um número
print('--'*28)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('--'*28)
jogador = int(input('Em que número pensei? ')) #Jogador tenta advinhar
print('PROCESSANDO...')
sleep(2)
if computador == jogador:
    print('Você venceu, parabéns!')
else:
    print('O computador venceu! O número pensado foi {}'.format(computador))
