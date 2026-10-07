soma = 1
n = 2


while 1/n >= 0.001:
    
    soma = soma + (1/n)
    n+=1


print(f"A soma é: {soma:.2f}")
print(f"Foram necessários: {n-1} termos")
