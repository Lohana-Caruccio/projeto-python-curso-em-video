import random
num = [1,2,3,4,5]
advinho = int(input('Advinhe em qual número estou pensando. De 1 a 5: '))
sorteio = random.choice(num)
if sorteio == advinho:
    print('Você venceu, parabéns!')
else:
    print('O computador venceu! O número pensado foi {}'.format(sorteio))