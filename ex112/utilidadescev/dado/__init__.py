#Entrada de dados monetários

def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '': #Conferir se é um string composta apenas por letras
            print(f'\033[31mERRO: "{entrada}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)

