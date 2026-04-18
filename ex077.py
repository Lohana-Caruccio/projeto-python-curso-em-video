#Contando vogais em Tupla
from time import sleep
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis','estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
print('-=-'*15)
print('QUANTAS VOGAIS TEMOS NAS PALAVRAS?')
print('-=-'*15)
sleep(1)
r = str(input('Vamos descobrir? [S/N] ')).upper().strip()[0]
while r not in 'SN':
    r = str(input('Vamos descobrir? [S/N] ')).upper().strip()[0]
if r in 'N':
    print(' ')
    print('Você que sabe 🤷‍♀️')
elif r in 'S':
    for p in palavras:
        print(f'\nNa palavra {p.upper()} temos: ', end='')
        for letra in p:
            if letra.upper() in 'AEIOU':
                print(f'{letra}', end=' ')



