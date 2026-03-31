#Jogo Jokenpô
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('{:-^70}'.format('👊🖐️✌️ \033[1;33mJOGO DE JOKENPÔ\033[m 👊🖐️✌️'))
print(' ')
print('''Suas opçòes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input('Qual a sua jogada: '))
if jogador != 0 and jogador != 1 and jogador != 2:
    print('Jogada inválida. Tente novamente.')
else:
 sleep(1)
 print('JO')
 sleep(1)
 print('KEN')
 sleep(1)
 print('PÔ!!!')
 sleep(1)
 print('-' * 25)
 print('Computador jogou {}.'.format(itens[computador]))
 print('Jogador jogou {}.'.format(itens[jogador]))
 print('-' * 25)
 if jogador == 0: #JOGADOR JOGOU PEDRA
     if computador == 1:
        print('COMPUTADOR VENCE! Papel embrulha pedra.')
     if computador == 2:
        print('JOGADOR VENCE! Pedra quebra tesoura.')
 elif jogador == 1: #JOGADOR JOGOU PAPEL
     if computador == 2:
        print('COMPUTADOR VENCE! Tesoura corta papel.')
     if computador == 0:
        print('JOGADOR VENCE! Papel embrulha pedra.')
 elif jogador == 2: #JOGADOR JOGOU TESOURA
     if computador == 0:
        print('COMPUTADOR VENCE! Pedra quebra tesoura.')
     if computador == 1:
        print('JOGADOR VENCE! Tesoura corta papel.')
 if computador == jogador:
    print('Tente mais uma vez, vocês EMPATARAM!')

