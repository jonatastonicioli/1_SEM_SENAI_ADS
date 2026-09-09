'''
Exercício 14

Peça ao usuário para digitar 10 números e armazene-os em uma lista.

Depois mostre:

Todos os números digitados.
O maior número (sem usar max()).
O menor número (sem usar min()).
Em qual posição da lista está o maior número.
Em qual posição da lista está o menor número.
'''

lista = []

for i in range(10):
    valor = int(input(f"Digite o valor {i}: "))
    lista.append(valor)
    
menor = lista[0]
maior = lista[0]
contadorMaior = 0
contadorMenor = 0

for i in range(len(lista)):
    if lista[i] < menor:
        menor = lista[i]
        contadorMenor = i
    if lista[i] > maior:
         maior = lista[i]
         contadorMaior = i

         
print("O menor valor é: ", menor," na posição: ", contadorMenor)

print("O maior valor é: ", maior," na posição: ", contadorMaior)
