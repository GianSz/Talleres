def MaximoComĂșnDivisor(a, b):
    if(a<b):
       return MaximoComĂșnDivisor(b, a)
    elif(b==0):
        return a
    else:
        return MaximoComĂșnDivisor(b, a%b)
 
a = int(input("Introduce el primer numero "))
b = int(input("Introduce el segundo numero "))
print("El MCD es", MaximoComĂșnDivisor(a, b))

print(a%b)