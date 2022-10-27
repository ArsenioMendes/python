def leiaint(msg):
    valor = 0
    ok = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO, DIGITE UM NÚMERO INTEIRO.\033[m ')
        if ok:
            break
    return valor


n = leiaint('DIGITE UM NÚMERO: ')
print(f'Você acabou de digitar o número {n}')

