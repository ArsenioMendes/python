def voto(ano):
    """
    -> Informe de obrigatoriedade de votação.
    :param ano: Data de nascimento do individuo.
    :return: Retorna a resposta (OBRIGATÓRIO, OPCIONAL, NÃO VOTA)
    """
    from datetime import date
    atual = date.today().year
    idade = atual - ano

    if idade <= 16:
        return f'Com {idade}: NÃO VOTA. '
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade}: VOTO OPCIONAL. '
    else:
        return f'Com {idade}: VOTO OBRIGATÓRIO. '


print(voto(int(input('Digite o ano de nascimento: '))))
