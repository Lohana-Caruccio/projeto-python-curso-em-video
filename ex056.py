cont = 0
Nm = 0
soma = 0
media = 0
maior = 0
cM = 0
for p in range(1,5):
    nome = str(input('{}ª pessoa- Digite seu nome: '. format(p))).strip().upper()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: ')).strip().upper()
    cont += 1
    soma = soma + idade
    if sexo == 'M':
     if p == 1:
         maior = idade
     else:
         if idade > maior:
            maior = idade
    if idade == maior:
        Nm = nome
    if sexo == 'F':
        if idade < 20:
            cM += 1
media = soma / cont
print('A média de idade entre essas 4 pessoas é de {:.0f} anos.'.format(media))
print('O nome do homem mais velho é {}'.format(Nm))
print('Das mulheres, {} tem menos de 20 anos.'.format(cM))

