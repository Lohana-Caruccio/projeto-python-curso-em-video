#Site está acessível?
import urllib.error #Importando módulos de erro
import urllib.request

try:
    headers = {'User-Agent': 'Mozilla/5.0'} #Definindo um "User-Agent" para simular um navegador comum
    req = urllib.request.Request('https://www.pudim.com.br', headers=headers)

    #Tentando abrir a requisição modificada
    site = urllib.request.urlopen(req)
except urllib.error.URLError:
    print(f'\033[31mERRO: Site não está acessível\033[m')
else:
    print('\033[34mTudo certo! Site acessível...\033[m')
