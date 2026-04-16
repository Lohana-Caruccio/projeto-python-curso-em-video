#Número por extenso
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte' )
num = int(input('Digite um número de 0 a 20: '))
while num not in range(0,21):
    num = int(input('Tente novamente. Digite um número de 0 a 10: '))
print(f'Você digitou o número {extenso[num]}!')
