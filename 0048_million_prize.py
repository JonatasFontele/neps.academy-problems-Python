# Problema Prêmio do Milhão
# OBI 2015 - Primeira Fase - Nível Júnior
N = int(input())
sum = 0
enough = False
for i in range(N):
    A = int(input())
    sum += A
    if sum >= 1000000 and not enough:
        print(i + 1)
        enough = True
