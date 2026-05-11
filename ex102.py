#Função para fatorial
def factorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do fatorial de um número n
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            if c == 1:
                print(f'{c}', end=' ')
            else:
                print(f'{c} x', end=' ')
    return f'= {f}'

#Programa principal
print(f'{"FATORIAL":^25}')
print(' ')
print(factorial(5, True))
print(' ')
help(factorial)