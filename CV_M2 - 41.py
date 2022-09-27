n1 = float(input("qual a nota da primeira unidade?"))
n2 = float(input("qual a nota da segunda unidade?"))

total = n1 + n2
media = total/2

if media > 7:
    print(f"aluno aprovado com {media} na media")
elif 5 < media < 6.9:
    print(f"recuperação com media {media} final")
else: print(f"aluno reprovado com media {media} final")