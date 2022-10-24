from datetime import date


def voto(ano):
    ano = idade
    print(f'Com {idade} anos:', end=' ')
    if 16 <= ano <= 18:
        print('VOTO OPCIONAL')
    elif ano <= 15:
        print('VOTO NEGADO')
    elif ano >= 70:
        print('VOTO OPCIONAL')
    else:
        print('VOTO OBRIGATÓRIO')


nascimento = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nascimento
voto(idade)
