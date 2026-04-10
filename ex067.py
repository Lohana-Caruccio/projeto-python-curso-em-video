#Tabuada
print('{: ^50}'.format('\033[1;35mPROGRAMA TABUADA\033[m'))
print(' ')
n = 0
while True:
    n = int(input('Digite um número para ver sua \033[4;35mTABUADA:\033[m '))
    print(' ')
    if n < 0:
        break
    else:
        c = 0
        for c in range(0,10):
            c += 1
            print(f'{n} x {c} = {n*c}')
    print(' ')
print('Fim do programa TABUADA! Volte sempre!')