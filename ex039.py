#Alistamento
print('\033[1;34;33mALISTAMENTO\033[m')
print(' ')
from datetime import date
nascimento = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - nascimento
if idade < 18:
    print('Faltam {} anos para você ter que se alistar!'.format(18 - idade))
elif idade > 18:
    print('Já passou {} anos do ano que você teria que ter se alistado!'.format(idade - 18))
else:
    print('Está na hora de você se alistar!')

