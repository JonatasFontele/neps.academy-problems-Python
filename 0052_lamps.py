# Problema Lâmpadas
# OBI 2016 - Primeira Fase - Nível Júnior
N = int(input())
I = map(int, input().split())
A, B = 0, 0  # Lâmpada A e B apagadas

for i in I:
    if i == 1:  # Interruptor I1
        A += 1
    if i == 2:  # Interruptor I2
        A += 1
        B += 1
print(A % 2)  # Módulo/resto da divisão por 2 gera 0 ou 1 para par ou ímpar
print(B % 2)
