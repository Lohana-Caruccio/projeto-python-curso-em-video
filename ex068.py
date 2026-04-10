#JOGO PAR OU ÍMPAR
from random import randint
print('-=-'*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-'*10)
v = 0
r = ''
while True:
    jogador = int(input('Diga um valor: '))
    comput = randint(0, 10)
    s = jogador + comput
    tipo = ' '
    while tipo not in 'PI':
        tipo= str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print('--'*15)
    print(f'Você jogou {jogador} e o computador jogou {comput}. Total deu {s}.', end=' ')
    print('\033[1m- PAR\033[m' if s % 2 == 0 else '\033[1m- ÍMPAR\033[m')
    if tipo == 'P':
        if s % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if s % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
    print('--'*15)
print('--'*15)
print(f'GAME OVER! Você venceu {v} vezes.')









