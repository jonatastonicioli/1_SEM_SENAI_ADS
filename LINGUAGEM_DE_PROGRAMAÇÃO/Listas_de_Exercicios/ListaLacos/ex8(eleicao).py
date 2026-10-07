
listaCandidatos = ["Lula", "Flavio", "Renan Santos"]

Cand1 = 0
Cand2 = 0
Cand3 = 0
Nulos = 0

print("[1] - Lula \n[2]- Flavio \n[3]- Renan Santos \n[4]- Anular \n[0]- Sair \nDigite o numero do seu candidato para votar: ")

while True:

    voto = int(input())

    match voto:

        case 1:
            print("Você votou no candidato 1")
            Cand1+=1
        case 2:
            print("Você votou no candidato 2")
            Cand2+=1
        case 3:
            print("Você votou no candidato 3")
            Cand3+=1
        case 4:
            print("Você anulou seu voto")
            Nulos+=1
        case 0:
            break

lista = [Cand1,Cand2,Cand3]
maior = max(lista)
indiceMaior = lista.index(maior) #vai ser usado para printar o candidato

#calculos porcentagem

totalVotos = Cand1 + Cand2 + Cand3 + Nulos

if totalVotos >0:

    porc1 = Cand1/totalVotos *100
    porc2 = Cand2/totalVotos *100
    porc3 = Cand3/totalVotos *100
    pNulos = Nulos/totalVotos *100

    print("======================Resultado======================")
    print("O vencedor da eleição é: ", listaCandidatos[indiceMaior])
    print("As porcentagens de cada candidato são: ")
    print(f"Lula - {porc1:.2f}%")
    print(f"Flávio - {porc2:.2f}%")
    print(f"Renan Santos - {porc3:.2f}%")
    print(f"Nulos - {pNulos:.2f}%")

else:
    print("Não houve nenhum voto!!!")











