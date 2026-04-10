#Vários números com flag
s = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    s += n
print('-=-'*15)
print(f'A soma de todos os números digitados foi {s}!')

