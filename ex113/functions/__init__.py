#Funções

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: Por favor digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print(f'\n\33[31mERRO: Entrada de dados intemrrompida pelo usuário.\033[m')
            return 0
        else:
            break
    return n

def leiaFlo(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: Por favor digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print(f'\n\33[31mERRO: Entrada de dados intemrrompida pelo usuário.\033[m')
            return 0
        else:
            break
    return n





