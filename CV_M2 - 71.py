n50 = n20 = n10 = n01 = 0
print('==================\nBANCO DO LADRÃO\n==================')
print('Sistema para saque ...')
saque = int(input('Digite um valor para realizar o saque: '))
total = saque
while saque > 50:
    n50 += 1
    saque -= 50
while saque > 20:
    n20 += 1
    saque -= 20
while saque >= 10:
    n10 += 1
    saque -= 10
while saque >= 1:
    n01 += 1
    saque -= 1

print(f'Serão sacadas:\n~~ {n50} notas de 50.00 R$\n~~ {n20} notas de 20.00 R$\n~~ {n10} notas 10.00 R$\n~~ {n01} notas de '
      f'1.00 R$\n~~ Total: {total:.2f} R$')
