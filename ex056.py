#Analisador Completo
soma = 0
media = 0
maior = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print('------{}ª PESSOA------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade
    if p == 1 and sexo in 'Mm':
         maior = idade
         nomevelho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
            totmulher20 += 1
media = soma / 4
print(' ')
print('A média de idade entre essas 4 pessoas é de {:.1f} anos.'.format(media))
print('O homem mais velho tem {} anos e seu nome é {}.'.format(maior, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))


