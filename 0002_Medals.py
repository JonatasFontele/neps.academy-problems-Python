# Problema Medalhas
# OBI 2016 - Segunda Fase - Nível Júnior

T1 = int(input())
T2 = int(input())
T3 = int(input())

if T1 < T2 < T3:
    print("1\n2\n3")
elif T1 < T3 < T2:
    print("1\n3\n2")
elif T2 < T1 < T3:
    print("2\n1\n3")
elif T2 < T3 < T1:
    print("2\n3\n1")
elif T3 < T1 < T2:
    print("3\n1\n2")
else:
    print("3\n2\n1")