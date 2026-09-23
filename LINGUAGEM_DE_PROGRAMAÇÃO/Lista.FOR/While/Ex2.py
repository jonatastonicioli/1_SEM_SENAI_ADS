maior = 0
i = 0

while i<5:
 num = int(input(f"Digite o numero {i}: "))
 i+=1
 
 if num > maior:
    maior = num

print(maior)