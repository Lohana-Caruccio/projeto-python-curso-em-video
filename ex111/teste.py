#Transformando módulos em pacotes

from ex111.utilidadescev import moeda

p = float(input("Digite o preço do produto: R$"))
moeda.resumo(p)