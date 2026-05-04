#Cadastro de Trabalhador em Python
from datetime import date
atual = date.today().year
cadastro = dict()
while True:
    cadastro['Nome']= str(input('Nome: ')).strip()
    nascimento = int(input('Ano de nascimento: '))
    idade = atual - nascimento
    cadastro['Idade'] = idade
    cadastro['Carteira de Trabalho'] = int(input('Carteira de trabalho (0 não tem): '))
    if cadastro['Carteira de Trabalho'] == 0:
        break
    elif cadastro['Carteira de Trabalho'] != 0:
        cadastro['Ano de contratação'] = int(input('Ano de contratação: '))
        cadastro['Salário'] = float(input('Salário: R$'))
        cadastro['Aposentadoria'] = cadastro['Idade'] + ((cadastro['Ano de contratação']+35)- atual)
        break
print('-='*30)
for k, v in cadastro.items():
    if k == 'Aposentadoria' or k == 'Idade':
        print(f'{k}: {v} anos')
    elif k == 'Salário':
        print(f'{k}: R${v}')
    else:
        print(f'{k}: {v}')


