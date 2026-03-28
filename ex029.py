vel = int(input('Em qual velocidade o carro está andando? '))
multa = (vel - 80) * 7
if vel > 80:
    print('Você ultrapassou a velocidade indicada.')
    print('Portanto, sua multa será de R${:.2f}.'.format(multa))

