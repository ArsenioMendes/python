num = int(input("qual o numero decimal que deseja operar?"))
bas = input("qual base numerica deseja operar? (1 para binário, 2 para octal, 3 para hexadecimal)")
res = 0

if bas == '1':
    print(f"o resultado do valor {num} em BINARIO e: ")
    res = bin(num)
    print(res[2::])
elif bas == '2':
    print(f"o resultado do valor {num} em OCTAL e: ")
    res = oct(num)
    print(res[2::])
else:
    print(f"o resultado do valor {num} em HEXADECIMAL e: ")
    res = hex(num)
    print((res[2::]))
    