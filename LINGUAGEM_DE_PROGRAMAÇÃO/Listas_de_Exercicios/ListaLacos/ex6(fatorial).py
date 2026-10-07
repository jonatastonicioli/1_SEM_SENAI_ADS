while True:

    num = int(input("Digite o numero para calcular o fatorial: "))

    if num<0:
        print("Digite um número positivo!!!")
        break

    else:

        i = num

        while i!=1:
            i-=1

            num = num * i

        print(f"O valor do fatorial é: {num}")  

        escolha = input("Você deseja continuar(S/N)?").lower()

    if escolha == 'n': #para o while true
        break






