# Problema Zerinho ou Um
A, B, C = map(int, input().split())

if A != B and B == C:
    print("A")
elif B != A and A == C:
    print("B")
elif C != A and A == B:
    print("C")
else:
    print("*")
