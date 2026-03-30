#Categoria de Natação
from datetime import date
print('\033[1;34mClassificando nadadores\033[m')
print(' ')
nasc = int(input('Digite o seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Sua categoria é MIRIM!'.format(idade))
elif idade <= 14:
    print('Sua categoria é INFANTIL!'.format(idade))
elif idade <= 19:
    print('Sua categoria é JUNIOR!'.format(idade))
elif idade <= 25:
    print('Sua categoria é SÊNIOR!'.format(idade))
else:
    print('Sua categoria é MASTER!'.format(idade))
