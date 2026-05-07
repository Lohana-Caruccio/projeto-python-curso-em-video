#Função que descobre o maior valor
from time import sleep
def maior (* num):
    print('-'*50)
    print(f'Analisando os valores passados...')
    c = ma = 0
    while c < len(num):
        if c == 0:
            ma = num[c]
        elif num[c] > ma:
            ma = num[c]
        print(f'{num[c]} ', end=' ')
        sleep(0.3)
        c += 1
    print(f'Foram informados {c} valores ao todo.')
    print(f'O maior valor informado foi {ma}.')

#Programa principal
maior(2,9,4,5,7,1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
