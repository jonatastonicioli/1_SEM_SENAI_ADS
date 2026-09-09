#8. Calcule o volume de um tronco de cone.
import math

raioMaior = float(input("Digite o raio maior: "))
raioMenor = float(input("Digite o raio menor: "))
altura = float(input("Digite a altura: "))

Volume = (1/3) * math.pi * altura * (raioMaior**2 + raioMenor**2 + raioMaior*raioMenor)

print(f"O volume do cone é: {Volume}")
