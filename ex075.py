#Análise de dados em uma Tupla
T = (int(input('Primeiro valor: ')),
     int(input('Segundo valor: ')),
     int(input('Terceiro valor: ')),
     int(input('Quarto valor: ')))
print(f'Você digitou os seguintes valores {T}')
print(f'O valor 9 apareceu {T.count(9)} vezes')
if 3 not in T:
    print('O número 3 não foi digitado em nenhuma posição')
else:
    print(f'O número 3 apareceu na {T.index(3)+1}ª posição ')
print('Os número pares digitados foram: ', end='')
for v in T:
    if v % 2 == 0:
        print(v, end=' ')








