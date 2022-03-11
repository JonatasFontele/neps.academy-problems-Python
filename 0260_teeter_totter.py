# Problema Gangorra
# OBI 2014 - Primeira Fase - Nível Júnior
PC = list(map(int, input().split()))

if PC[0] * PC[1] == PC[2] * PC[3]:
    print(0)
elif PC[0] * PC[1] > PC[2] * PC[3]:
    print(-1)
else:
    print(1)
    