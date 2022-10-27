c = ('\033[49m',  # 0 - SEM COR
     '\033[0;30;41m',  # 1 - VERMELHO
     '\033[0;30;42m',  # 2 - VERDE
     '\033[0;30;44m',  # 3 - AZUL
     '\033[107m',     # 4 - BRANCO
     )


def ajuda(cmd):
    print(c[4], end='')
    help(cmd)
    print(c[0], end='')


def titulo(msg, cor=0):
    print(c[cor], end='')
    print(f'~' * (len(msg) + 5))
    print(f'  {msg}')
    print(f'~' * (len(msg) + 5))
    print(c[0], end='')


comando = ''
while True:
    titulo('Sitema HelpAetorian', 3)
    print(c[3], end='')
    comando = str(input('Função ou Biblioteca > '))
    print(c[0], end='')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até Logo', 3)
