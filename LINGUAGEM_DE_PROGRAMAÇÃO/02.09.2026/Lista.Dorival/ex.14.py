#14. Crie duas variáveis, a e b, com valores escolhidos pelo usuário. Troque os valores
#dessas variáveis sem usar uma terceira variável e imprima os novos valores de a e b.

a = int(input("Digite o  valor a: "))
b = int(input("Digite o valor b: "))

a,b = b,a

print(a)
print(b)