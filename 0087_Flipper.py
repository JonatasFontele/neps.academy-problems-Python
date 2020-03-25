# Problema Flíper
# OBI 2014 - Primeira Fase - Nível Júnior
P, R = input().split()

P = int(P)
R = int(R)

if P == 1 and R == 1:
    print("A")
elif P == 1 and R == 0:
    print("B")
else:
    print("C")