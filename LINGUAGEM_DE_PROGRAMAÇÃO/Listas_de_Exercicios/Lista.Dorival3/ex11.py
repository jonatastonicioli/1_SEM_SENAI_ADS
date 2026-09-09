# 11. Calcule o cosseno da lei dos cossenos para encontrar um lado.

a = float(input("Digite o lado a: "))
b = float(input("Digite o lado b: "))
c = float(input("Digite o lado c: "))

cos = ((a**2) + (c**2) - (b**2)) / (2*a*c)

print(f"O valor do cosA é: {cos:.2f}")


