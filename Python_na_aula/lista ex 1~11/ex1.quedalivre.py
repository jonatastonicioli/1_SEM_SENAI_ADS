'''
Exercício — Queda Livre

Um objeto é abandonado de uma determinada altura e cai em queda livre.

Considere:

A aceleração da gravidade:
g = 9,8 m/s²

A velocidade inicial:
v0 = 0

A altura final:
h = 0


A equação do movimento é:

h = h0 + v0*t + (1/2)*g*t²


Determine o tempo necessário para o objeto atingir o solo.


O programa deve:

1. Solicitar ao usuário a altura inicial h0.

2. Verificar se a altura informada é válida.

3. Calcular o tempo de queda.

4. Exibir o resultado.


Caso a altura seja negativa, mostrar:

Altura inválida: a altura não pode ser negativa


Dados:

g = 9.8
v0 = 0
h = 0


Fórmula utilizada:

t = sqrt((2*h0)/g)


'''
import math

g = 9.8

v0 = 0

h = 0

h0 = float(input("Digite a altura h do objeto: "))

if(h0<0):
    print("Altura inválida: a altura não pode ser negativa")
    exit()

t = math.sqrt((2*h0)/g) # ou t = ((2*h0)/g) ** (1/2)
# ** é operador de potencia 

print(f"O tempo é de {t:.2f} segundos") 


#g*t^2 = 2* h0
#h = h0 + v0*t + (1/2)*g*t^2