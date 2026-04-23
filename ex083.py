#Validando expressões matemáticas
expr = str(input('Digite a expressão: '))
pilha = list()
for simb in expr:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop() #remove o simbolo colocado na pilha
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está certa!')
else:
    print('Sua expressão está errada!')

