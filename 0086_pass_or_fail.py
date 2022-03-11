# Problema Aprovado ou Reprovado
A, B = map(float, input().split())

average = (A + B) / 2

if average >= 7:
    print("Aprovado")
elif average >= 4:
    print("Recuperacao")
else:
    print("Reprovado")
