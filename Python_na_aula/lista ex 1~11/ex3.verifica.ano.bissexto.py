'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

ano = int(input("Digite o ano a ser verificado?: "))

if  ano%4 == 0 and ano%100 != 0: 
    print("O ano é bissexto")
    
elif ano%400 == 0:
    print("O ano é bissexto")
    
else: 
    print("O ano não é bissexto")
    
    
    
