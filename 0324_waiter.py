# Problema Garçom
# OBI 2010 - Primeira Fase - Nível Júnior
N = int(input())
copos = 0

for i in range(N):
    LC = list(map(int, input().split()))
    if LC[0] > LC[1]:
        copos += LC[1]
print(copos)