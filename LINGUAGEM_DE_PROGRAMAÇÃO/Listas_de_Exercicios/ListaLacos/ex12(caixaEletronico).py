saldoInicial = 1000
saldoFinal = 0
contNotas100 = 0
contNotas50 = 0

while (True):
    print("="*6, " Menu", "="*6)
    print("[a] - Depositar \n[b] - Sacar \n[c] - Ver Saldo \n[d]- Sair")

    escolha = input("Digite sua escolha: ")

    match (escolha):
        case 'a': 
            valorDeposito = float("Digite o valor a ser depositado: ")

            if valorDeposito>0:
                saldoFinal = saldoInicial + valorDeposito
            else:
                print("Digite um valor positivo")

        case 'b':
            valorSaque = float(input("Digite o valor do saque: "))

            if valorSaque % 2 == 0:
                if valorSaque % 100 == 0:
                    contNotas100 += 1

                elif (valorSaque - contNotas100*100) % 50 == 0:
                    contNotas50 +=1

                    print(f"{contNotas100} {contNotas50}")

                else:
                    ...
                
            else:
                print("O valor do saque deve ser multiplo de 2!!!")



