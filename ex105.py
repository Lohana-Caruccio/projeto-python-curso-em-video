#Analisando e gerando dicionários
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos.(aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicioanr a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    info = dict()
    info['total'] = len(n)
    info['maior'] = max(n)
    info['menor'] = min(n)
    info['media'] = round(sum(n)/len(n), 2) #Usa-se o round para arredondamento
    if sit:
        if info['media'] >= 7:
            info['sit']= 'BOA'
        elif 5 <= info['media'] < 7:
            info['sit'] = 'RAZOÁVEL'
        elif info['media'] < 5:
            info['sit'] = 'RUIM'
    return info

resp = notas(7.5,6.5,2.8, sit=True)
print('_'*80)
print(resp)
help(notas)