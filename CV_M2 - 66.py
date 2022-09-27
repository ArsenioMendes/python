num = total = termos = 0
while True:
    num = int(input('Digite um número: '))
    total += num
    termos += 1
    if num == 999:
        break
print(f'~~Foram registrados {termos} números\n~~Na soma total de {total}.')