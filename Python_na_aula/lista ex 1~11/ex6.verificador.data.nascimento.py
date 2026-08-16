# Escreva um programa que peça ao usuário que insira um dia, mês e ano de
# nascimento. O programa deve verificar se a data é válida no calendário
# gregoriano. Deve considerar meses com 30 ou 31 dias, e o mês de fevereiro
# com 28 ou 29 dias (dependendo se o ano informado for bissexto). O ano de
# nascimento não pode ser anterior a 1900.

from datetime import date

ano_atual = date.today().year # retorna o ano, usado para impedir ano futuro

dia = int(input("Digite seu dia de nascimento: "))
mes = int(input("Digite seu mês de nascimento: "))
ano = int(input("Digite seu ano de nascimento: "))

anobissexto = False
diavalido = False


#Verificação meses com 30 dias
if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia > 30:
        diavalido = False
    elif dia > 0 :
        diavalido =  True
    else: #desnecessário, pois ja é falso naturalmente
        diavalido = False

#Verificação meses com 31 dias
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes== 8 or mes == 10 or mes == 12:
    if dia > 31:
        diavalido = False
    elif dia > 0:
        diavalido = True
    else: #desnecessário, pois ja é falso naturalmente
        diavalido = False

#Verificador de ano bissexto, verifica só se for fevereiro
if mes == 2:

    if  ano%4 == 0 and ano%100 != 0: 
        anobissexto = True
    
    elif ano%400 == 0:                  
        anobissexto = True
    
    else:  #desnecessário, pois ja é falso naturalmente
        anobissexto = False            

#Verificação de fevereiro
if anobissexto == True and mes==2:
    if dia>29:
        diavalido = False
    elif dia > 0 :
        diavalido =  True
    else: #desnecessário, pois ja é falso naturalmente
        diavalido = False

if anobissexto == False and mes==2:
    if dia>28:
        diavalido = False
    elif dia > 0 :
        diavalido =  True
    else: #desnecessário, pois ja é falso naturalmente
        diavalido = False

if diavalido == True and ano>=1900 and ano<=ano_atual:
    print("A sua data de nascimento é válida!")
else: 
    print("A sua data de nascimento NÃO é válida!")
