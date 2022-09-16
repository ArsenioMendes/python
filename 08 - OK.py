fai_1: int = 0  # até 15 anos
fai_2 = 0  # até 30 anos
fai_3 = 0  # até 45 anos
fai_4 = 0  # até 60 anos
fai_5 = 0  # acima de 60 anos
x = 0

for n in range(1, 6):
    x = int(input(f"qual a idade da pessoa {n}"))
    n + 1
    if x < 15:
        fai_1 += 1
    elif x < 30:
        fai_2 += 1
    elif x < 45:
        fai_3 += 1
    elif x < 60:
        fai_4 += 1
    else:
        fai_5 += 1
print(f"faixa 1={fai_1}")
print(f"faixa 1={fai_2}")
print(f"faixa 3={fai_3}")
print(f"faixa 4={fai_4}")
print(f"faixa 5={fai_5}")

print(f"porcentagem de pessoas na faixa 1 = {fai_1*100/5}%")
print(f"porcentagem de pessoas da faixa 5 = {fai_5*100/5}%")