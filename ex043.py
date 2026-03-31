#Calculando o IMC
print('\033[1;31;44mCálculo de IMC\033[m')
print(' ')
peso = float(input('Digite seu peso atual(kg): '))
altura = float(input('Digite sua altura(m): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é de {:.1f}, você está \033[1;34mABAIXO\033[m do peso ideal!'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é de {:.1f}, você está com peso \033[1;32mIDEAL!\033[m'.format(imc))
elif 25 <= imc <30:
    print('Seu IMC é de {:.1f}, você está com \033[1;31mSOBREPESO!\033[m'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é de {:.1f}, você está com \033[1;31mOBESIDADE!\033[m'.format(imc))
else:
    print('Seu IMC é de {:.1f}, você está com \033[1;31mOBESIDADE MÓRBIDA!\033[m'.format(imc))

