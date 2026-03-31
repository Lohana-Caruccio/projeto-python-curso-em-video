#Calculando o IMC
print('\033[1;31;44mCálculo de IMC\033[m')
print(' ')
peso = float(input('Digite seu peso atual: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Seu IMC é de {:.2f}, você está \033[1;34mABAIXO\033[m do peso!'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é de {:.2f}, você está com peso \033[1;32mIDEAL!\033[m'.format(imc))
elif imc >= 25 and imc <= 30:
    print('Seu IMC é de {:.2f}, você está com \033[1;31mSOBREPESO!\033[m'.format(imc))
elif imc >= 30 and imc <= 40:
    print('Seu IMC é de {:.2f}, você está com \033[1;31mOBESIDADE!\033[m'.format(imc))
else:
    print('Seu IMC é de {:.2f}, você está com \033[1;31mOBESIDADE MÓRBIDA!\033[m'.format(imc))
