#Ficha do Jogador
def ficha(no='<desconhecido>', go=0):
    print(f'O jogador {no} fez {go} gol(s) no campeonato.')

nome = str(input('Digite o nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(go=gols)
else:
    ficha(nome, gols)
