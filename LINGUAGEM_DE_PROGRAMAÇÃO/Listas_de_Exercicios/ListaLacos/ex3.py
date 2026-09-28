senha = "bomdia"
contador = 0

while contador != 3:
    senhaUser = input("Digite a senha: ")
    contador += 1

    if senhaUser == senha:
        print("Você entrou no sistema")
        break

    else:
        print("Senha incorreta")
        

if contador == 3 and senhaUser != senha:
    print("Seu acesso foi bloqueado")

print(f"Foram usadas {contador} tentativas")

        

    





