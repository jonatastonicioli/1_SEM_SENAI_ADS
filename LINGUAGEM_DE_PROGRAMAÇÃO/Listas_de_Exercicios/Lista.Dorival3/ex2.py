#2. Leia três números e calcule média aritmética, geométrica e harmônica.

num1 = int(input("Digite o num1: "))
num2 = int(input("Digite o num2: "))
num3 = int(input("Digite o num3: "))

mediaAritmetica = (num1 + num2 + num3) / 3
mediaGeometrica = (num1 * num2 * num3) ** (1/3)
mediaHarmonica = 3 / ((1/num1) + (1/num2) + (1/num3))

print(f"A media aritmética é: {mediaAritmetica:.2f}")
print(f"A media geometrica é: {mediaGeometrica:.2f}")
print(f"A media harmonica é: {mediaHarmonica:.2f}")