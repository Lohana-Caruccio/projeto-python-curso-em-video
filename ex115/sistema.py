#SISTEMA SIMPLES DE CADASTRO

from ex115.lib.arquivo import *
from time import sleep

#1- Conferir se o arquivo existe, se não existe, será criado
arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

#2- Programa principal
while True:
    resp = menu(['Listar pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])
    if resp == 1:
        #Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho('Saindo do sistema!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1.5)
