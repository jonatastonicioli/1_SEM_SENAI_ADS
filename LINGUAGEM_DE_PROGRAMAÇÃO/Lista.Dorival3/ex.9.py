import math

#9. Aplique a fórmula de Heron para área de um triângulo.

a = float(input("Digite o lado a: "))
b = float(input("Digite o lado b: "))
c = float(input("Digite o lado c: "))

p = a+b+c

A = math.sqrt(p(p-a)(p-b)(p-c))

print(f"A área é: {A}")