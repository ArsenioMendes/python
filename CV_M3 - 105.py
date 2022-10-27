def notas(*n, sit=False):
    """
    -> Dicionário de notas.
    :param n: Refere-se ao Dicionário
    :param sit: Informa a situação geral das notas
    :return: Dicionário com: TOTAL-MAIOR-MENOR-MEDIA
    """
    ficha = {'total': len(n), 'maior': max(n), 'menor': min(n)}
    media = sum(n) / len(n)
    ficha['media'] = media
    if sit:
        if media > 7:
            ficha['situação'] = 'BOA'
        else:
            ficha['situação'] = 'RUIM'

    return ficha


resp = notas(5.5, 3.5, 7.2, 4.7, sit=True)
print(resp)
