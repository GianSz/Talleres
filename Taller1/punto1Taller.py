def MaximoComúnDivisor(a, b):
    if(a<b):
       return MaximoComúnDivisor(b, a)
    elif(b==0):
        return a
    else:
        return MaximoComúnDivisor(b, a%b)
 
a = int(input("Introduce el primer numero "))
b = int(input("Introduce el segundo numero "))
print("El MCD es", MaximoComúnDivisor(a, b))

print(a%b)