import math

def print_calculadora():
    a = '''_______________________
        |  ___________________   |
        | |                   |  |
        | |       123456      |  |
        | |___________________|  |
        |                        |
        |  +-----+ +-----+ +---+ |
        |  |  7  | |  8  | | 9 | |
        |  +-----+ +-----+ +---+ |
        |                        |
        |  +-----+ +-----+ +---+ |
        |  |  4  | |  5  | | 6 | |
        |  +-----+ +-----+ +---+ |
        |                        |
        |  +-----+ +-----+ +---+ |
        |  |  1  | |  2  | | 3 | |
        |  +-----+ +-----+ +---+ |
        |                        |
        |  +-----+ +-----+ +---+ |
        |  |  0  | |  .  | | = | |
        |  +-----+ +-----+ +---+ |
        |                        |
        |  +-----+ +-----+ +---+ |
        |  |  +  | |  -  | | x | |
        |  +-----+ +-----+ +---+ |
        |                        |
        |  +-----------+ +-----+ |
        |  |    /      | |  C  | |
        |  +-----------+ +-----+ |
        |________________________|  '''

    return a

print(print_calculadora())

def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def divisao(a,b):
    return a/b

def multiplicar(a,b):
    return a*b

def raiz(a):
    return a**2

def potencia (a,b):
    return a**b

def porcentagem(a,b):
    return (a/b) * 100

def pedir_1_numero():
    return

def pedir_2_numeros():
    a = int(input("Digite o número 1: "))
    b = int(input("Digite o número 2: "))
    return (a,b)

def printar_resultado(resultado):
    
    return print(f"O resultado é: {resultado}")

def main():
    print(print_calculadora)

    opcao = input("Digite a operação que vc quer realizar: ")

    match opcao:
        case "+":
            num1,num2 = pedir_2_numeros()
            resultado = soma(num1,num2)

        case "-":
            num1,num2 = pedir_2_numeros()
            resultado = subtracao(num1,num2)

        case "*":
            num1,num2 = pedir_2_numeros()
            resultado = multiplicar(num1, num2)
        case "/":
            num1,num2 = pedir_2_numeros()
            resultado = divisao(num1,num2)
        case "r":
            num1 = pedir_1_numero()
            resultado = raiz(num1)
        case "p":
            num1,num2 = pedir_2_numeros()
            resultado = potencia(num1, num2)
        case "por":
            num1,num2 = pedir_2_numeros()
            resultado = porcentagem(num1,num2)
    
    printar_resultado(resultado)

            


        

main()










