import random

a = random.randint(1, 10)
b = random.randint(1, 10)
c = random.randint(1, 10)
d = random.randint(1, 10)
e = random.randint(1, 10)

num = (a, b, c, d, e)
maior = max(num)
menor = min(num)

print(f'Os valores listados : {num}')
print(f'o maior valor é {maior}')
print(f'o menor valor é {menor}')