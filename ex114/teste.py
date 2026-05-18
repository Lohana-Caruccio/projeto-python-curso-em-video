#Site está acessível?
import urllib.error #Importando módulos de erro
from urllib.request import urlopen, Request

try:
    headers = {'User-Agent': 'Mozilla/5.0'} #Definindo um "User-Agent" para simular um navegador comum
    req = Request('https://www.pudim.com.br', headers=headers)

    #Tentando abrir a requisição modificada
    site = urlopen(req)
except urllib.error.URLError:
    print(f'\033[31mERRO: Site Pudim não está acessível.\033[m')
else:
    print('\033[34mTudo certo! Site acessível...\033[m')
