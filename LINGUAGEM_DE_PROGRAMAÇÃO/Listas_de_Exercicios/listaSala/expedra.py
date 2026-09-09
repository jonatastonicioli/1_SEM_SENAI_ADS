import random

lista = ["Pedra", "Papel", "Tesoura"]

print("Oque você deseja escolher: ")
print("[0] - Pedra")
print("[1] - Papel")
print("[2] - Tesoura")

escolhaUsuario = int(input("Digite a opção desejada! "))

escolhaPC = random.choice(lista)

if lista[escolhaUsuario] == escolhaPC:
    print("O jogo EMPATOU")
elif escolhaUsuario == 0 and escolhaPC == lista[2] or  escolhaUsuario == 1 and escolhaPC == lista[0] or escolhaUsuario == 2 and escolhaPC == lista[1]:
    print("Você ganhou")
else:
    print("Você perdeu")

print(f"O computador escolheu: {escolhaPC}")
print(f"O você ")


#0,1,2 papel, tesoura , pedra 0 , 1  (player1 - player2 + 3) % 3 