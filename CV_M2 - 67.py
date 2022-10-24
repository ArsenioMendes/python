num = resultado = mult = 0
while True:
    num = int(input('Digite um valor para expressar na tabuada: '))
    if num < 0:
        break
    for c in range(1, 11):
        mult = c * num
        print(f'~~ {num} X {c} = {mult}')
print('fim do código.')