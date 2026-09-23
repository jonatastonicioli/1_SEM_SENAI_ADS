num = int(input("Digite o número a ser calculado o fatorial: "))
contador = num - 1

while contador>0:
    num = num * contador
    contador -= 1

print (num)