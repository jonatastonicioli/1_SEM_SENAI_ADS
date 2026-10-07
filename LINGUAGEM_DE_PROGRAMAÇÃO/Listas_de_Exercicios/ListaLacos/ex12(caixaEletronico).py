saldoInicial = 1000
saldoFinal = 0
contNotas100 = 0
contNotas50 = 0
contNotas20 = 0
listaOperacoes = []

while (True):
    print("="*6, " Menu", "="*6)
    print("[a] - Depositar \n[b] - Sacar \n[c] - Ver Saldo \n[d]- Sair")

    escolha = input("Digite sua escolha: ")

    match (escolha):
        case 'a': 
            valorDeposito = float(input("Digite o valor a ser depositado: "))
            listaOperacoes.append("Deposito")


            if valorDeposito>0:
                saldoFinal = saldoInicial + valorDeposito
            else:
                print("Digite um valor positivo")


        case 'b':

            contNotas100 = 0
            contNotas50 = 0
            contNotas20 = 0
            contNotas10 = 0
            contNotas5 = 0
            contNotas2 = 0
            listaOperacoes.append("Saque")
            
            valorSaque = float(input("Digite o valor do saque: "))

            if valorSaque > saldoFinal:
                print("O valor do saque não pode ser maior que o saldo")
                continue 

            if valorSaque % 2 == 0:

                # contNotas100 = valorSaque // 100
                # contNotas50 = (valorSaque%100) // 50
                # contNotas20 = (valorSaque%100)%50 // 20
                # contNotas10 = ((valorSaque%100)%50)%10 // 10
                # contNotas5 = (((valorSaque%100)%50)%10)%5 // 10

                restante = valorSaque

                ContNotas100 = restante//100
                restante = restante % 100

                ContNotas50 = restante//50
                restante  restante % 50

                ContNotas20 = restante//20
                restante = restante % 20

                ContNotas10 = restante // 10
                restante = restante % 10

                ContNotas5 = restante // 5
                restante = restante % 5

                ContNotas2 = restante // 2
                restante = restante % 2

                saldoFinal = saldoFinal - ContNotas100*100 - ContNotas50 *50 - ContNotas20*20 - ContNotas5*5 - ContNotas2 *2                         

            # print(f"n100: {ContNotas100} n50: {ContNotas50} n20: {ContNotas20} n10: {ContNotas10} n5: {ContNotas5}") 
            # print(f"O saldo final é: {saldoFinal}")

            else:
             print("O valor do saque deve ser multiplo de 2!!!")

        case 'c':
            print(f"Seu saldo é: {saldoFinal}")
            listaOperacoes.append("Ver Saldo")
            
        case 'd':
             print("="*6, "FIM DO PROGRAMA", "="*6)
             print("As operações realizadas são:", listaOperacoes)
             break
           


            
                
          



