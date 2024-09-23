def notas(*n, sit=False):
    '''
    :param n: números das notas
    :param sit: True para ver a situação
    :return: um dicionário com informações sobre as notas fornecidas
    '''

    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5 and r['média'] < 7:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'

    return r


resp = notas(7, 9, 10, 8, 7, sit=True)
print(resp)

help(notas)
