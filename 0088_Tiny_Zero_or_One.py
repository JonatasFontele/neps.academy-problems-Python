# Problema Zerinho ou Um
A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

if A != B and B == C:
    print("A")
elif B != A and A == C:
    print("B")
elif C != A and A == B:
    print("C")
else:
    print("*")