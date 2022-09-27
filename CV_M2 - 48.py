#TABUADA

n = int(input('digite um valor para calcular na tabuada: '))
r = 0
print(f'Tabuada do número {n}')
print("---------------------------")
for c in range(1, 11):
    r = n*c
    print(f'{n}X{c}={r}'