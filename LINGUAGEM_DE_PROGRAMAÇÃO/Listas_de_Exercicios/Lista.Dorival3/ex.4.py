#4. Calcule o MMC de dois números usando apenas operações aritméticas conhecidas
#(sem if; pode usar fórmulas).
import math

num1 = int(input("Digite o num1: "))
num2 = int(input("Digite o num2: "))

mdc = math.gcd(num1,num2)

MMC = (num1 * num2 )// mdc

print(f"O MMC é: {MMC}")
