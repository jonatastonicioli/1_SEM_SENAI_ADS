num = int(input("Digite o numero desejado: "))
contador = 0
maior = num

while num !=1: #enquanto o numero e diferente de 1 executa 

    if num<0:
        print("Digite um valor positivo")
        break
    else:
        if num %2 == 0:
            num = num/2
            contador += 1
            print(num)
        else:
            num = 3*num + 1
            contador += 1
            print(num)

    if num > maior:
        maior = num
print(f"Foram necessárias {contador} interações")
print(f"O maior número atingido é: {maior}")