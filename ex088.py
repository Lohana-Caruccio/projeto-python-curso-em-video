#Palpites para a Mega Sena
from random import randint
from time import sleep
print('-'*40)
print(f'{"\033[4;33mJOGOS PARA A MEGA SENA\033[m":^49}')
print('-'*40)
opcoes = list()
jogo = list()
pergunta = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= pergunta:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()
    opcoes.append(jogo[:])
    jogo.clear()
    tot += 1
print('-='*4, f'SORTEANDO {pergunta} JOGOS', '-='*4)
sleep(1)
for i, o in enumerate(opcoes):
    print(f'Jogo {i+1}: {o}')
    sleep(1)
print(' ')
print('-='*4, f'BOA SORTE', '-='*4)




