# Lâmpadas
# OBI 2016 - Primeira Fase - Nível Júnior
N = int(input())
I = input().split()

for i in range(len(I)): # Transformar todos os elementos da lista de string para inteiros
    I[i] = int(I[i])

A = 0 # Lâmpada A apagada
B = 0 # Lâmpada B apagada

for i in range(len(I)):
    if I[i] == 1: # Interruptor I1
        A += 1
    if I[i] == 2: # Interruptor I2
        A += 1
        B += 1
print(A % 2) # Módulo/resto da divisão por 2 gera 0 ou 1 para par ou ímpar
print(B % 2)