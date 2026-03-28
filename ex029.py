vel = int(input('Qual a velocidade atual do carro? '))
multa = (vel - 80) * 7
if vel > 80:
    print('Você ultrapassou a velocidade indicada.')
    print('Portanto, sua multa será de R${:.2f}.'.format(multa))

print('Tenha um bom dia, e dirija com segurança!')

