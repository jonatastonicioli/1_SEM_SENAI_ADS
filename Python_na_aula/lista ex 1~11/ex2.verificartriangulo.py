'''
Exercício 2 — Classificação de Triângulos

Escreva um programa que peça ao usuário três valores correspondentes aos lados de um triângulo.

Primeiro, verifique se os valores formam um triângulo válido (a soma de dois lados deve ser sempre maior que o terceiro).

Se não formar, exiba um erro.

Se formar, classifique-o em:

- Equilátero
- Isósceles
- Escaleno

Além disso, verifique se ele é um triângulo retângulo (usando o Teorema de Pitágoras). '''

num1 = int(input("Digite o valor do lado 1: "))
num2 = int(input("Digite o valor do lado 2: "))
num3 = int(input("Digite o valor do lado 3: "))

if num1 + num2 > num3 and num2 + num3 > num1 and num1 + num3 > num2:
    if num1 == num2 == num3:
        print("O triângulo é equilátero")
    elif num1 == num2 or num1==num3 or num2==num3:
        print("O triângulo é isósceles")
    else:
        print("O triângulo é escaleno")
            
else: 
    print("O triângulo é impossível, programa encerrado")
    exit()
    
if num1**2 + num2**2 == num3**2 or num1**2 + num3**2 == num2**2 or num2**2 + num3**2 == num1**2:
 print("O triângulo é retângulo")