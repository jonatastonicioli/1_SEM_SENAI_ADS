'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

'''Crie um programa que peça uma senha ao usuário. A senha deve ser classificada como:
"Inválida": Menos de 8 caracteres.
"Fraca": Só letras minúsculas ou números.
"Média": Mistura de letras e números.
"Forte": Letras maiúsculas, minúsculas, números e pelo menos um caractere especial (!, @, #, $, etc.).'''

a = input("Digite sua senha: ")

acumuladorAlpha = False
acumuladorNumerico = False
acumuladorUpper = False
acumuladorLower = False
ehEspecial = False

for i in a: #percorrendo a string caracter por caracter o i esta recebendo a

    ehAlpha=str.isalpha(i) #verifica se é alfanumerico, se for muda a variavel acumulador para true
    if ehAlpha == True:
        acumuladorAlpha = True
        
    ehNumerico=str.isnumeric(i) #verifica se é numerico, se for muda a variavel acumulador para true
    if ehNumerico == True:
        acumuladorNumerico = True
        
    ehUpper=str.isupper(i) #verifica se é maiuscula, se for muda a variavel acumulador para true
    if ehUpper == True:
        acumuladorUpper = True

    ehLower=str.islower(i) #verifica se é minuscula, se for muda a variavel acumulador para true
    if ehLower == True:
        acumuladorLower = True
    
    if ehNumerico == False and ehAlpha == False:
        ehEspecial = True
        
    
if len(a)<8:
    print("A senha é inválida pois tem menos de 8 caractetes")
elif str.islower(a) and str.isalpha(a):  
    print("A senha é fraca, pois so tem letras minúsculas")
elif str.isnumeric(a):
    print("A senha é fraca, pois so tem números")
elif acumuladorAlpha == True and acumuladorNumerico== True and ehEspecial == False:
    print("A senha é média pois mistura letras e números")
elif acumuladorUpper == True and acumuladorNumerico == True and acumuladorLower == True and ehEspecial==True:
    print("A senha é forte, tem letra maiúscula, letra minúscula, número e caracter especial")
else: 
    print("A senha não atende aos requisitos mínimos")
    



#print(type(a))