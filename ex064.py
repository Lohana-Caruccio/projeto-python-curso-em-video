#Tratando valores
num = cont = soma = 0
while num != 999:
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
     cont = cont + 1
print(' ')
print('Você digitou {} números e a soma entre eles foi {}!'.format(cont, soma))
