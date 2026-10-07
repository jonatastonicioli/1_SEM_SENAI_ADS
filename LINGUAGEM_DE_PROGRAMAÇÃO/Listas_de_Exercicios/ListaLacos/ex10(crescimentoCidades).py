ano = 0

popA = 1000 
popB = 5000 


while popA<popB:

    popA = popA + popA*0.03
    popB = popB + popB*0.015
    

    ano+=1

print(f"Foram necessários: {ano} anos")
print(f"A população A é: {popA:.0f}")
print(f"A população B é: {popB:.0f}")
    