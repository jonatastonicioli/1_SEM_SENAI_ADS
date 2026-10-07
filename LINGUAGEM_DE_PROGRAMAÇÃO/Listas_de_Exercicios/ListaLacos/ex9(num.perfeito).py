num = int(input("Digite o número a ser verificado: "))
divisores = []

for i in range (1, num):

    if num % i == 0:
        divisores.append(i)

print("Os divisores são: ", divisores)

if sum(divisores) == num:
    print("O número é perfeito")
else:
    print("O número não é perfeito")
    