print('-=-'*9)
print('Analisando um triângulo...')
print('-=-'*9)
comp1 = float(input('Digite o comprimento da primeira reta: '))
comp2 = float(input('Digite o comprimento da segunda reta: '))
comp3 = float(input('Digite o comprimento da terceira reta: '))
if comp1 < comp2 + comp3 and comp2 < comp1 + comp3 and comp3 < comp1 + comp2:
    print(' ')
    print('Esses segmentos PODEM formar um triângulo')
else:
    print(' ')
    print('Esses segmentos NÃO PODEM formar um triângulo')
