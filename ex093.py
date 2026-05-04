#Cadastro de Jogador de futebol
cadastro = dict()
cadastro['nome'] = str(input('Nome do jogador: ')).strip()
partidas = int(input(f'Quantas partidas {cadastro["nome"]} jogou? '))
gols = list()
for c in range(0,partidas):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
cadastro['gols'] = gols
cadastro['total'] = sum(gols)
print('-'*35)
print(cadastro)
print('-'*35)
for k, v in cadastro.items():
    print(f'O campo {k} tem o valor {v}.')
print('-'*35)
print(f'O jogador {cadastro["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(cadastro['gols']):
    print(f'  => Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {cadastro["total"]} gols.')
