# Programa que simula o saque de um caixa eletrônico.
# O usuário informa o valor a ser sacado. O programa deve informar quantas
# notas de 100, 50, 20, 10, 5 e 2 serão entregues, priorizando sempre as
# notas de maior valor. Se o valor não puder ser sacado com as notas
# disponíveis (ex: R$1, R$3), o programa deve informar
# "Valor impossível de sacar com as notas disponíveis".

valor = float(input("Digite o valor a ser sacado: "))

Notas100 = 0
Notas50 = 0
Notas20 = 0
Notas10 = 0
Notas5 = 0
Notas2 = 0

resto = 0

Notas100 = int(valor/100)
resto = valor - Notas100*100

Notas50 = int((resto)/50)
resto = resto - Notas50*50

   
Notas20 = int((resto)/20)
resto = resto - Notas20*20

         
Notas10 = int((resto)/10)
resto = resto - Notas10*10

            
Notas5 = int((resto)/5)
resto = resto - Notas5*5

              
Notas2 = int((resto)/2)
resto = resto - Notas2*2

if resto != 0:
 print("Valor impossível de sacar com as notas disponíveis")
 exit()
        
print("Serão entregues: ")
print(Notas100, 'notas de 100;')
print(Notas50, 'notas de 50;')
print(Notas20, 'notas de 20;')
print(Notas10, 'notas de 10;')
print(Notas5, 'notas de 5;')
print(Notas2, 'notas de 2;')

     
        




