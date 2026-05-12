#Validando entrada de dados em Python
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

#Programa principal
print(f'{"\033[34mVamos ver se o número é inteiro?\033[m":^50}')
while True:
    n = leiaInt('\nDigite um número: ')
    print('-='*18)
    print(f'Você acabou de digitar o número {n}.')
    r = str(input('\nQuer continuar? [S/N] ')).strip().upper()[0]
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break
print('\nFIM DO PROGRAMA!')
