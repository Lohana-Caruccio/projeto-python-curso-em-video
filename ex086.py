#Matriz em Python
print('--'*15)
print(f'{"\033[1;36mCRIANDO UMA MATRIZ 3x3\033[m":^40}')
print('--'*15)
matriz = [[0,0,0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3): #1o for para alimentar os espaços com os valores
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print('-'*40)
for l in range(0, 3): #2o for para estruturar e mostrar na tela
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end = ' ')
    print() #quebra toda vez que começar uma nova linha
