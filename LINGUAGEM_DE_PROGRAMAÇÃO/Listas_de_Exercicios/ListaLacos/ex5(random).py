import random

num=0
cont = 0

numRandomico = (random.randint(1,100))


while numRandomico !=num:

    num = int(input("Digite o número: "))

    cont+=1

    if(numRandomico ==num):
        print("PARABÉNS, vc acertou!!!")
        break

    print(f"O numero randomizado é: {numRandomico}")

    if abs(numRandomico-num) > 20:
        print("Muito alto, a diferença é maior que 20")
    
    elif abs(numRandomico-num) >= 10:
        print("Alto, a diferença é maior ou igual a 10 mas menor que 20")

    elif abs(numRandomico-num) >= 5:
            print("Baixo, a diferença e maior ou igual a 5 mas menor que 10")

    else:
            print("Muito Baixo, a diferença é menor que 5")

    print(f"Você tem mais {10-cont} tentativas")

    if cont == 10:
          break


    
