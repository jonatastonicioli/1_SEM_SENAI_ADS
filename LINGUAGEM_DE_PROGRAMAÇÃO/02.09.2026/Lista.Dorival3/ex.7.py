#7. Calcule a área de um hexágo no regular dado o lado.

lado = float(input("Digite o valor do lado: "))

area = (3 * (lado**2) * (3 **(1/2)))/2

print(f"A área do hexágono é : {area:.2f}")