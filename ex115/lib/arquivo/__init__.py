#Manipulação do arquivo
from ex115.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #"rt"- read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #"wt+"- write text and create file
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for lin in a:
            dado = lin.split(';') #Corta a linha do arquivo onde tiver um ponto e vírgula
            if len(dado) == 2:
                dado[1] = dado[1].replace('\n', '')
                print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome= 'desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} criado com sucesso!')