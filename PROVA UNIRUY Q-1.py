import random

num = entre20_80 = total = 0

while True:
    num = random.randint(0, 100)
    if 20 >= num <= 80:
        entre20_80 += 1
    total += 1
    if total == 15:
        break

print(f'Valores entre 20 e 80 = {entre20_80} valores. ')