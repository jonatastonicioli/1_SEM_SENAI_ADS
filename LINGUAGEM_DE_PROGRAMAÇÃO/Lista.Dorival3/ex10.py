# 10. Calcule a distância entre dois pontos em 3D.

xa = float(input("Digite o valor Xa: "))
ya = float(input("Digite o valor Ya: "))
za = float(input("Digite o valor Za: "))


xb = float(input("Digite o valor Xb: "))
yb = float(input("Digite o valor Yb: "))
zb = float(input("Digite o valor Zb: "))

distancia = ((xb - xa)**2 + (yb-ya)**2 + (zb-za)**2) ** (1/2)

print(f"A distância entre 2 pontos é: {distancia:.2f}")