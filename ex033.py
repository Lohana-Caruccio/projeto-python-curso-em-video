num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))
#Verificando quem é o menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
#Verificando quem é o maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))