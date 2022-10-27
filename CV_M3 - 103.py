def ficha(jogador, gols_marcados=0):
    """
    -> Validação de ficha de gols
    :param jogador: Nome do jogador.
    :param gols_marcados: Gols marcados pelo jogador.
    :return: Nome e quantidade de gols do jogador.
    """
    print(f'O jogador {jogador}, marcou {gols_marcados} gols.')


n = str(input('Digite o nome do jogador: '))
g = int(input('Digite a quantidade de Gols: '))
if n.strip() == '':
    n = '<DESCONHECIDO>'
    ficha(jogador=n, gols_marcados=g)
else:
    ficha(n, g)
