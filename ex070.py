#Estatísticas em produtos
total = mais1000 = cont = maisB = nomeB = 0
print('__' * 20)
print('{:^38}'.format('LOJA BARATÃO'))
print('__' * 20)
while True:
    nomeP = str(input('Nome do produto: ')).strip()
    valor = float(input('Preço: R$'))
    cont += 1
    total += valor
    if valor > 1000:
        mais1000 += 1
    if cont == 1:
        maisB = valor
        nomeB = nomeP
    elif valor < maisB:
        maisB = valor
        nomeB = nomeP
    print('-' * 20)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-' * 20)
    if resp == 'N':
        break
print('FIM DO PROGRAMA')
print(' ')
print(f'O total da compra foi R${total:.2f}')
print(f'Dos produtos comprados, {mais1000} custam mais de R$1000,00')
print(f'O produto mais barato foi: \033[1m{nomeB}\033[m e ela custa {maisB}')