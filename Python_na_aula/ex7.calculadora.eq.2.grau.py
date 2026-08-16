"""
7. Faça um programa que calcula o resultado de uma equação de 2° grau.
   Peça os coeficientes a, b e c.
   - Se a for zero, avise que "Não é uma equação de segundo grau".
   - Se for, calcule o discriminante (Δ). Se Δ < 0, exiba
     "A equação não possui raízes reais".
   - Se Δ = 0, calcule e exiba a raiz única.
   - Se Δ > 0, calcule e exiba as duas raízes.
"""
a = float(input("Digite o coeficiente 'a': "))
b = float(input("Digite o coeficiente 'b': "))
c = float(input("Digite o coeficiente 'c': "))

delta = (b**2 - 4*a*c) # exponenciação é ** e não ^ 

if a==0:
    print("Não é uma equação de segundo grau")

elif delta == 0:

    # realizando os calculos dentro do if para não dar divisão por zero
    r1 = (-b + delta**(1/2))/(2*a)
    r2 = (-b - delta**(1/2))/(2*a)
    print("A raiz é unica, cujo valor é {}".format(r1)) #.format para printar melhor, nao precisa do f string
elif delta < 0:
    print("A equação não possui raízes reais")
else:
    r1 = (-b + delta**(1/2))/(2*a)
    r2 = (-b - delta**(1/2))/(2*a)
    print("A equação possui duas raízes reais que são: r1 = {} e r2= {}".format(r1,r2))