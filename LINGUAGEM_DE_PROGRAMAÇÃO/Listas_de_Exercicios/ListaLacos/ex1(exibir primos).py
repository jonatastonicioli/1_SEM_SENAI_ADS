inicio = int(input("Digite o valor do inicio: "))
final = int(input("Digite o valor final: "))
contador = 0 

for j in range (inicio, final):

    #verificador numero primo
    ehPrimo = True
    for i in range(2,j):
        if j % i == 0:
            ehPrimo = False

    if ehPrimo: #se ehPrimo for true vai printar
        contador = contador + 1

        print(f"{j} {contador}")