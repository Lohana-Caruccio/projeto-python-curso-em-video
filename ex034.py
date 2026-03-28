salario = float(input('Qual é o seu salário? R$'))
if salario > 1250:
    print('Seu aumento de salário foi de 10%, somando um novo total de R${:.2f}!'.format(salario*1.1))
else:
    print('Seu aumento de salário foi de 15%, somando um novo total de R${:.2f}!'. format(salario*1.15))