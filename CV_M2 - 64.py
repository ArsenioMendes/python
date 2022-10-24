total = 0
num = 0
termos = 0
while num != 999:
    num = int(input('digite um valor: '))
    total += num
    termos += 1
print(f'A soma de {termos} termos foi = {total}')