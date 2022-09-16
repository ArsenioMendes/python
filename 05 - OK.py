
c = str(input("qual o nome do cliente?: "))
v = int(input("quanto foi o total de compras no ano passado ?: "))

if v>1000:
    v = v*1.15
    print("o valor com bonus de 15% é =", v)
else:
    v = v*1.10
    print("o valor com bonus de 10% é =", v)
