#15. Crie três variáveis, nota1, nota2 e nota3, com valores escolhidos pelo usuário.
#Calcule a média ponderada dessas notas, onde os pesos são 2, 3 e 5,
#respectivamente. Imprima o resultado.

nota1 = float(input("Digite o valor da nota 1: "))
nota2 = float(input("Digite o valor da nota 2: "))
nota3 = float(input("Digite o valor da nota 3: "))

media = (nota1*2 + nota2*3 + nota3*5) / (2+3+5)

print(f"A média ponderada é: ", media)

