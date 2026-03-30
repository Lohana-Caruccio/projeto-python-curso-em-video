#Alistamento
from datetime import date
print('\033[1;34;33mALISTAMENTO\033[m')
print(' ')
atual = date.today().year
nascimento = int(input('Digite o seu ano de nascimento: '))
idade = atual - nascimento
if idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Você tem {} anos.\nFaltam {} anos para você ter que se alistar!\nSeu alistamento será '
          'no ano de {}.'.format(idade,saldo, ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Você tem {} anos.\nDeveria ter se alistado há {} anos.\nSeu alistamento foi em {}.'.format(idade,saldo,ano))
else:
    print('Você tem {} anos.\nEstá na hora de você se alistar!'.format(idade))

