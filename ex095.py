#Aprimorando os Dicionários
cadastro = list()
jogador = dict()
while True:
    print('_'*35)
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = list()
    for c in range(0,partidas):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    cadastro.append(jogador.copy())
    while True:
        r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if r in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if r in 'Nn':
        break
print('_'*50)
print('cod ', end=' ')
for i in jogador.keys(): #LOOP PARA MOSTRAR TÍTULO DA TABELA - Para cada posição(i) do dicionário "jogador"
    print(f'{i:<15} ', end='') #Será printado cada key(i) na mesma linha
print()
print('-'*50)
for c, v in enumerate(cadastro): #LOOP PARA MOSTRAR TABELA - For para ler dentro de uma lista(cadastro)
   print(f'{c:>3}  ', end=' ') #Mostra o código dos jogadores
   for d in v.values(): #Mostra os valores dentro dos dados que estão dentro do dicionário(jogador) que está dentro da lista(cadatsro)
       print(f'{str(d):<15}', end=' ')#d significa dado
   print()
print('-'*50)
while True:
    dados = int(input('Mostrar dados de qual jogador [999 para parar]? '))
    if dados == 999:
        break
    if dados >= len(cadastro):
        print(f'ERRO! Não existe jogador com código {dados}!')
        print('-'*35)
    else:
        print('_'*35)
        print(f'---LEVANTAMENTO DO JOGADOR {cadastro[dados]["nome"]}') #Entramos dentro da lista(cadastro) na posição "dados" e utilizamos o value guardado na key nome
        for i, g in enumerate(cadastro[dados]['gols']): #Pega cada índice dentro da lista "gols", conta e mostra o valor tido em cada partida
            print(f'  => Na partida {i + 1}, fez {g} gols')
        print('_'*35)
print('<< VOLTE SEMPRE >>')

