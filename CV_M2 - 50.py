# Progressão Aritmética

r = int(input('qual a razão da PA?: '))
x = int(input('qual o primeiro termo da PA?: '))
y = 0
res = 0

for c in range(1, 11):
    y = c * r
    res = y + x
    print(f'{c} termo da PA = {res}')
