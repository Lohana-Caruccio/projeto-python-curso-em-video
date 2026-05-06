#Um print especial
def escreva(txt):
    print('~' * (len(txt) + 4))
    print(f'  {txt}')
    print('~' * (len(txt) + 4))

while True:
    frase = str(input('Escreva uma frase: ')).strip()
    escreva(frase)
    r = ' '
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('\n<<FIM DO PROGRAMA>>')