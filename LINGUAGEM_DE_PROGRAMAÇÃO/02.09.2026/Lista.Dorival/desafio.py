#DESAFIO
#16. Crie quatro variáveis, x1, y1, x2 e y2, representando as coordenadas de dois
#pontos no plano cartesiano (por exemplo, x1 = 1, y1 = 2, x2 = 4, y2 = 6). Os
#valores devem ser solicitados pelo usuário. Calcule a distância entre esses dois
#pontos usando a fórmula da distância euclidiana

x1 =  int(input("Digite o valor x1: "))
y1 =  int(input("Digite o valor y1: "))
x2 =  int(input("Digite o valor x2: "))
y2 =  int(input("Digite o valor y2: "))

deltaY = y2 - y1 
deltaX = x2 - x1

distancia = ((deltaX)**2 + (deltaY)**2)**(1/2)

print(f"A distância entre os dois pontos é: {distancia:.2f}")