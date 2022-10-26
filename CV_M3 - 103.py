def ficha(nome=0, gols=0):

    if nome == 0:
        print(f'O jogador <DESCONHECICO> fez {gols} gol(s)')
    else:
        print(f'O jogador {nome} fez {gols} gol(s)')


name = str(input('Digite o nome do jogador: '))
goals = int(input('Digite a quantidade de Gols: '))
ficha(name, goals)
