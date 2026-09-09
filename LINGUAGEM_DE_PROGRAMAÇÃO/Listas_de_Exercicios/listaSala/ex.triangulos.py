a = float(input("Digite o lado a: "))
b = float(input("Digite o lado b: "))
c = float(input("Digite o lado c: "))

if a+b>c and a+c>b  and b+c>a:
    if a==b and a==c and b==c:
        print("O triângulo é equilátero")
    elif a!=b and a!=c and b!=c:
        print("O triângulo é escaleno")
    else:
        print("O triângulo isósceles")
else:
    print("Não é possível formar um triângulo")
        
     