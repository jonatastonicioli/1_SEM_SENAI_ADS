def maior (x,y):
    if x>y:
        return x
    else:
        return y
    
num1 = int(input("Digite o valor 1: "))
num2 = int(input("Digite o valor 2: "))

print ("O maior valor é: ",maior(num1,num2))