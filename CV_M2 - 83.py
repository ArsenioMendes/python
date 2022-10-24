parenteses = []

palavra = str(input('Digite uma expressão: '))

for c in palavra :
    if c in '(':
        parenteses.append('(')
    elif c in ')':
        if len(parenteses) > 0:
            parenteses.pop(0)
        elif len(parenteses) == 0:
            parenteses.append(')')
            print('Expressão inválida. ')
            break

if len(parenteses) == 0:
    print('Expressão válida.')

print('codigo finalizado.')
            


