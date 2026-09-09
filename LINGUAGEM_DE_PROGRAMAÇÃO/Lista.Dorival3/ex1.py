#Declare variáveis para massa e velocidade e calcule a energia cinética.

massa = int(input("Digite a massa: "))
velocidade = int(input("Digite a velocidade: "))

energiaCinetica = ((massa) * (velocidade**2))/2

print(f"A energia cinética é: {energiaCinetica}")