def sumaRecursiva(lista, indice = 0):

    if(indice == len(lista)-1):
        return lista[indice]
    
    else:
        return lista[indice] + sumaRecursiva(lista, indice + 1)

print("-----------------------------------------------------------------------------------------------------------------------------------")
print("A continuación habrá un espacio para ingresar los números a sumar, para dejar de ingresar números por favor ingresar el caractér '*'")
print("-----------------------------------------------------------------------------------------------------------------------------------")

numero = input("Ingrese el numero que desea ingresar al arreglo: ")
arr = []
while(numero != '*'):

    try:
        arr.append(int(numero))
    except(ValueError):
        print("Ha ingresado un valor diferente a un caratér numérico y al caractér '*'.Vuelva a intentarlo.")
    numero = input("Ingrese el numero que desea ingresar al arreglo: ")


print("El resultado de la suma es:")
print(sumaRecursiva(arr))