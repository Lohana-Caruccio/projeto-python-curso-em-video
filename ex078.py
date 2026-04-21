#Maior e Menor valores na Lista
valores = list()
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
print('--'*20)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)}, econtrado nas posições ', end= '')
for pos, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{pos} ... ', end='')
print(f'\nO menor valor digitado foi {min(valores)}, encontrado nas posições ', end= '')
for pos, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{pos}...', end='')
