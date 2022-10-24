ano = int(input("qual o ano de nascimento do atleta"))
idade = 2022 - ano

if idade < 9:
    print(f"atleta mirim com {idade} anos")
elif idade < 14:
    print(f"altleta infantil com {idade} anos")
elif idade <19:
    print(f"atleta junior com {idade} anos")
elif idade < 20:
    print(f"atleta senior com {idade} anos")
else: print(f'atleta master com {idade} anos')

