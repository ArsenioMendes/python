import random
turnos = soma = num_c = num_j = 0
esco = 'p'

print('===Jogo do Impar ou Par===')
while True:
    num_j = int(input('Escolha um número: '))
    num_c = random.randint(1, 11)
    soma = num_c + num_j
    esco = str(input('Escolha entre Impar ou Par: ')).strip().upper()[0]
    print(f'Escolha do PC -> {num_c}')
    if esco == 'P':
        if soma % 2 == 0:
            print('Vitoria do jogador')
            turnos += 1
            print(f'->-> {turnos} Vitorias registradas <-<-')
        else:
            print(
                f'================================\nDerrota, encerrando programa\n~~Foram registradas {turnos} Vitorias.')
            break
    if esco == 'I':
        if soma % 2 != 0:
            print('Vitoria do Jogador')
            turnos += 1
            print(f'->-> {turnos} Vitorias registradas <-<-')
        else:
            print(
                f'================================\nDerrota, encerrando programa\n~~Foram registradas {turnos} Vitorias.')
            break
