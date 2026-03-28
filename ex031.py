dist = float(input('Qual a distância em km da sua viagem? '))
if dist <= 200:
    print('O valor da sua passagem será R${:.2f}'.format(dist * 0.50))
else:
    print('O valor da sua passagem será de R${:.2f}'.format(dist * 0.45))