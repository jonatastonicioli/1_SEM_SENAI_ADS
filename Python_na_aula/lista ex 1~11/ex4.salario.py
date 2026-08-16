'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

salario = float(input("Digite o salario?: "))

if salario < 2000:
    imposto = 0
    
elif salario < 4000:
    imposto = (salario - 2000)*0.1
    
elif salario < 8000:
    imposto = 200 + (salario - 4000)*0.2  #mais 200 pois e o máximo da faixa anterior
    
else: 
    imposto = 200 + 800 + (salario - 8000)*0.3 # mais 800 e 200 por causa das faixas anterires
    
salariof = salario - imposto

print("O salário final é: ", salariof)
print("O imposto é: ", imposto)
print("O salário bruto é", salario)

    
    


    
