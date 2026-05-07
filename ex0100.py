#Funções para sortear e somar
from time import sleep
from random import randint
def sorteia(lista):
    c = 0
    while c < 5:
        lista.append(randint(1,10))
        c += 1
    print(' ')
    print(f'Sorteando 5 valores da lista: ', end=' ')
    for n in numeros:
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO!')

def soma_par(nu):
    soma = 0
    for n in nu:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma}!')

print('\033[2;35mCriando e somando valores de uma lista...\033[m')

numeros = list()
sorteia(numeros)
soma_par(numeros)
