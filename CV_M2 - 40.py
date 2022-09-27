ano = int(input("qual seu ano de nascimento?"))

idade = 2022 - ano

if idade < 18:
    print("não é hora de se alistar")

    print(f"faltam: {idade - 18}, anos para se alistar.")
elif idade > 19:
    print("já passou da hora de se alistar")
    print(f"já se passaram {idade - 18} anos, que venceu o alistamento")
else:
    print("está na hora de se alistar")
