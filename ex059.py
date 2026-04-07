#Criando Menu de opções
from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opc = 0
while opc != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opc = int(input('>>>> Qual é a sua opcão? '))
    if opc == 1:
        soma= num1 + num2
        print('A soma entre {} e {} é {}'.format(num1, num2, soma))
    elif opc == 2:
        produto = num1 * num2
        print('A multiplicação de {} x {} é {}'.format(num1, num2, produto))
    elif opc == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('Entre {} e {}, o maior valor é {}'.format(num1, num2, maior))
    elif opc == 4:
        print('Informe os números novamente')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opc == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente.')
    print('--' * 15)
    sleep(2)
print('Fim do programa! Volte sempre!')

