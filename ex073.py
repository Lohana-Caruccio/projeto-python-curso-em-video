qualificacao = ('Palmeiras', 'Flamengo', 'São Paulo', 'Fluminense', 'Bahia', 'Athletico-PR', 'Coritiba',
                'Atlético Mineiro', 'Bragantino', 'Vitória', 'Botafogo', 'Grêmio', 'Vasco', 'Internacional',
                'Santos', 'Corinthians', 'Cruzeiro', 'Remo', 'Chapecoense', 'Mirassol')
print('-'*30)
print(f'Lista de times do Brasileirão:')
print(' ')
c = 1
for q in range(len(qualificacao)):
    print(f'{c:>2}º {qualificacao[q]:<20}')
    c = c + 1
print('-'*30)
print(f'Os 5 primeiros colocados foram: {qualificacao[:5]}')
print(f'Os últimos 4 colocados foram: {qualificacao[-4:]}')
print(f'Times em ordem alfabética: {sorted(qualificacao)}')
print(f'O Chapecoense está na {qualificacao.index("Chapecoense")+1}ª posição!')
