num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))
if num1 > num2 and num1 > num3:
    print('O {} é o maior número'.format(num1))
    if num2 > num3:
        print('O {} é o menor número'.format(num3))
    else:
            print('O {} é o menor número'.format(num2))
if num1 < num2 and num1 < num3:
    print('O {} é o menor número'.format(num1))
    if num2 < num3:
        print('O {} é o maior número'.format(num3))
    else:
        print('O {} é o maior número'.format(num2))
else:
    if num2 > num3:
        print('O {} é o maior número e o {} é o menor'.format(num2, num3))
    else:
        print('O {} é o maior número e o {} é o nenor'.format(num3,num2))

