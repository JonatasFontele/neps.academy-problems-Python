# Problema Consecutivos
# OBI 2012 - Primeira Fase - Nível 1

N = int(input())
V = input().split() # Lista de String
V = [int(V[i]) for i in range(len(V))] # Transformar todos os elementos da lista de string para inteiros
longest_sequence = 0  # Tamanho da maior sequencia
current_sequence = 1  # Tamanho da sequencia atual (estamos representando que o primeiro elemento representa uma sequência de tamanho 1)

for i in range(1, N):
    if V[i] == V[i - 1]:
        current_sequence += 1  # Se o número atual é igual ao anterior o tamanho da sequência aumenta
    else:
        current_sequence = 1  # Se o número é diferente, começamos uma nova sequência

    if (current_sequence > longest_sequence):
        longest_sequence = current_sequence  # Se o tamanho da sequência que estamos avaliando é maior do que a que tinhamos antes, atualizamos o tamanho da maior sequência.

print(longest_sequence)
