#Vários números com flag
s = c = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    c += 1
    s += n
print('-=-'*15)
print(f'A soma de todos os {c} números digitados foi {s}!')

