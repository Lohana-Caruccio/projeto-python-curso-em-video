#Jogo de Dados em Python
from operator import itemgetter #pega um item específico dentro de um dicionário, sendo item[0] uma key e item [1] um valor
from random import randint
from time import sleep
print(f'{"JOGANDO OS DADOS...":^40}')
sleep(1)
jogadores = dict()
for c in range(1,5):
    jogadores[c] = randint(1,6)
    print(f'O jogador {c} tirou {jogadores[c]} no dado')
    sleep(1)
print('-='*16)
print('=='*3, f'RANKING DOS JOGADORES', '=='*3)
print(' ')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: jogador{v[0]} com {v[1]}')
    sleep(1)
print(' ')
print(f'{"PARABÉNS A TODOS!":^32}')
