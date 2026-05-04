#Unindo dicionários e listas
lista = list()
cadastro = dict()
c = media = idades =0
while True:
    cadastro['nome'] = str(input('Nome: '))
    while True:
        cadastro['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if cadastro['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    cadastro['idade'] = int(input('Idade: '))
    idades += cadastro['idade']
    lista.append(cadastro.copy())
    c += 1
    cadastro.clear()
    r = ' '
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r in 'Nn':
        break
media = idades / c
print('-='*35)
print(f'Foram cadastradas {c} pessoas.')
print(f'A média de idade do grupo é {media:.0f} anos.')
print(f'As mulheres cadastradas foram: ', end = '')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end = '')
print()
print(f'As pessoas cadastradas com idade acima da média foram: ')
for p in lista:
    if p['idade'] >= media:
        print(f'- {p["nome"]}')
print('-'*20)
print('\n<<PROGRAMA ENCERRADO>>')