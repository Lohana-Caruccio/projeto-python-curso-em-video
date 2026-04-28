#Boletim com listas compostas
geral = list()
media = 0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    geral.append([nome, [nota1, nota2], media]) #Feito somente um append para simplificar, deixando-o já organizado
    r = ' '
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break
print('-='*20)
print(f'{"No.":<5}{"NOME":<10}{"MEDIA":>10}') #Print formatado nos espaços
print('--'*20)
for i, a in enumerate(geral): #o "a" é fixo, pois vai mostrar sempre o conteudo inteiro dentro do índice dado atual, que muda a cada laço
    print(f'{i:<4}', f'{a[0]:<10}', f'{a[2]:>8.1f}') #Mostra o índice, mostra o nome e mostra a média
print('-' * 50)
while True:
    N = int(input('Mostrar notas de qual aluno?(999 interrompe): '))
    print(' ')
    if N == 999:
        print('Finalizando...')
        break
    else:
        if N < len(geral):
            print(f'Notas de {geral[N][0]} são {geral[N][1]}') #mostra o nome dado pelo índice e informado pelo "0", e as notas achadas pelo índice dado e informado na posição "1"
            print(' ')
        else:
            print('Número não encontrado!')
            print(' ')



















