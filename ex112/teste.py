#Entrada de dados monetários

from ex112.utilidadescev import moeda, dado

p = dado.leiaDinheiro("Digite o preço do produto: R$")
moeda.resumo(p,20,35)
