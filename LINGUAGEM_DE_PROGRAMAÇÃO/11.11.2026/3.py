def somar_pontos(fase1, fase2):
    soma = fase1 + fase2

    if soma <= 100:
        print("Pontuação insuficiente, tente denovo!\n")
    
print("Teste 1:\n")
somar_pontos(60,50)
print("Teste 2:\n")
somar_pontos(30,40)