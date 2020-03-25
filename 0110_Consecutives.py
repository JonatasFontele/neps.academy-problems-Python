# Problema Consecutivos
# OBI 2012 - Primeira Fase - Nível 1

N = int(input())
V = input().split() # Lista de String

for i in range(len(V)): # Transformar todos os elementos da lista de string para inteiros
    V[i] = int(V[i])

longestSequence = 0  # Tamanho da maior sequencia
currentSequence = 1  # Tamanho da sequencia atual (estamos representando que o primeiro elemento representa uma sequência de tamanho 1)

for i in range(1, len(V)):
    if V[i] == V[i - 1]:
        currentSequence += 1  # Se o número atual é igual ao anterior o tamanho da sequência aumenta
    else:
        currentSequence = 1  # Se o número é diferente, começamos uma nova sequência

    if (currentSequence > longestSequence):
        longestSequence = currentSequence  # Se o tamanho da sequência que estamos avaliando é maior do que a que tinhamos antes, atualizamos o tamanho da maior sequência.

print(longestSequence)