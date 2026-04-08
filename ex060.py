#Cálculo de fatorial com alguns comentários para melhor entendimento
n = int(input('Digite um número para calcular seu fatorial: '))
cont = n #recebe n
fatorial = 1 #recebe 1 para depois utilizá-lo na multiplicação
print('Calculando {}! = '.format(n), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='') #vai printar o x até o último número da multiplicação ser 1, depois disso vai printar =
    fatorial = fatorial * cont  #acumula desde de 1(que era seu valor inicial) x 5(ex de contador inicial) e vai acumulando, (5(novo valor)) x 5 - 1 x (4(acumula o novo valor)) x 4 - 1 ... até o final, a cada laço
    cont = cont - 1  # diminui 1 do número enquanto o cont for maior que 0 e atua em conjunto do fatorial
print('{}'.format(fatorial)) #resultado acumulado