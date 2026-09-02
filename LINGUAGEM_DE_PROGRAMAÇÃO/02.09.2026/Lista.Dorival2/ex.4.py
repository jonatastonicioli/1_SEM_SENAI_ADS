#4. Declare duas variáveis a e b, e peça valores inteiros a elas. Realize a troca de
#conteúdo entre a e b. Exiba os valores antes da troca e depois da troca.

a = int(input("Digite o valor a: "))
b = int(input("Digite o valor b: "))

print(f"Os valores antes da troca são: a = {a}, b = {b}")

a,b = b,a

print(f"Os valores depois da troca são: a = {a}, b = {b}")



