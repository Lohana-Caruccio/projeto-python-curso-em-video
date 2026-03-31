#Analisando triângulo part2
print('Classificando triângulos...')
print(' ')
comp1 = float(input('Digite o primeiro segmento: '))
comp2 = float(input('Digite o segundo segmento: '))
comp3 = float(input('Digite o terceiro segmento: '))
if comp1 < comp2 + comp3 and comp2 < comp1 + comp3 and comp3 < comp1 + comp2:
    print('Esses segmentos PODEM formar um triângulo', end = ' ')
    if comp1 == comp2 == comp3:
        print('\033[4mEQUILÁTERO!\033[m')
    elif comp1 != comp2 != comp3 != comp1:
        print('\033[4mESCALENO!\033[m')
    else:
        print('\033[4mISÓSCELES!\033[m')
else:
    print('Esses segmentos NÃO PODEM formar um triângulo!')

