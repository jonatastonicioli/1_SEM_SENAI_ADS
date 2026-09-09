#12. Crie uma variável preco com o valor escolhido pelo usuário. Converta esse valor
#para uma string e concatene com a string "O preço é R$". Imprima o resultado.

preco = float(input("Digite o valor: "))

conversao = str(preco)

print(f"O preço é R$ {conversao}")