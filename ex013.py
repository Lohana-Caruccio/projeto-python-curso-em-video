n = float(input('Qual é o seu salário atual? R$'))
aum = (n * 15/100)
novosalario = n + aum
print('Você recebeu um aumento de 15%! E agora seu salário será de R${:.2f}.'.format(novosalario))