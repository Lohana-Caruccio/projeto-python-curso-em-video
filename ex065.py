pergunta = ''
cont = soma = media = maior = menor = 0
while pergunta != 'N':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / cont
print('--' * 20)
print('Você digitou {} números e média entre todos os valores foi {:.2f}'.format(cont,media))
print('O maior valor digitado foi {} e o menor foi {}!'.format(maior, menor))