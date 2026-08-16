# Faça um programa que leia a hora inicial, minuto inicial, hora final e
# minuto final de um jogo. Calcule a duração do jogo. O jogo pode começar
# em um dia e terminar no outro, mas a duração máxima é de 24 horas e
# 1 minuto. Exiba o resultado no formato "O jogo durou X hora(s) e
# Y minuto(s)."

listaInicial = [] #forçando o uso das listas
listaFinal = []
listaDelta = []

horaInicial = int(input("Digite a hora inicial: "))
listaInicial.append(horaInicial)

minutoInicial = int(input("Digite o minuto inicial: "))
listaInicial.append(minutoInicial)

horaFinal = int(input("Digite a hora final: "))
listaFinal.append(horaFinal)

minutoFinal = int(input("Digite o minuto final: "))
listaFinal.append(minutoFinal)

somaInicial = listaInicial[0]*60 + listaInicial[1]
somaFinal = listaFinal[0]*60 + listaFinal[1]

if(somaInicial<somaFinal):
    deltaMinuto = (somaFinal - somaInicial)
else:
    deltaMinuto = (somaFinal+60*24 - somaInicial)

if deltaMinuto >= 60:
    listaDelta.append(int(deltaMinuto/60))
    resto = deltaMinuto%60
    listaDelta.append(resto)
else:
    listaDelta.append(0)
    listaDelta.append(deltaMinuto) #colocando na posição 1 da lista para na hora de printar sair certo

#print(listaDelta)

print("O jogo durou {} horas e {} minutos".format(listaDelta[0], listaDelta[1]))




