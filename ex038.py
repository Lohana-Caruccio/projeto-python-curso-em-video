#Comparando valores
num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
if num1 > num2:
    print('O número {} é maior.'.format(num1))
elif num1 < num2:
    print('O número {} é maior.'.format(num2))
else:
    print('Não existe valor maior, os dois são iguais.')