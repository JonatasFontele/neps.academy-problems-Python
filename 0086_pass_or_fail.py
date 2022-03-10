# Problema Aprovado ou Reprovado
score1, score2 = input().split()

score1 = float(score1)
score2 = float(score2)
average = (score1+score2)/2

if average >= 7:
    print("Aprovado")
elif 4 <= average < 7:  # average >= 4 and average < 7:
    print("Recuperacao")
else:
    print("Reprovado")
