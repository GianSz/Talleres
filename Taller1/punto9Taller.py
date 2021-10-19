def oredenarLista(arr, indice = 0):

    if(indice == len(arr)-2):
        if(arr[indice] > arr[indice+1]):
            arr[indice], arr[indice+1] = arr[indice+1], arr[indice]
            


    else:

        posMenor = indice
        for i in range(indice+1, len(arr)):

            if(arr[posMenor] > arr[i]):
                posMenor = i

        arr[indice], arr[posMenor] = arr[posMenor], arr[indice]

        oredenarLista(arr, indice+1)

print("-----------------------------------------------------------------------------------------------------------------------------------")
print("A continuación habrá un espacio para ingresar números a un arreglo, para dejar de ingresar números por favor ingresar el caractér '*'")
print("-----------------------------------------------------------------------------------------------------------------------------------")

numero = input("Ingrese el numero que desea ingresar al arreglo: ")
arr = []
while(numero != '*'):

    try:
        arr.append(int(numero))
    except(ValueError):
        print("Ha ingresado un valor diferente a un caratér numérico y al caractér '*'.Vuelva a intentarlo.")
    numero = input("Ingrese el numero que desea ingresar al arreglo: ")

print("")
print("La lista sin ordenar es la siguiente: ")
print(arr)

oredenarLista(arr)

print("Así quedaría la lista ordenada: ")
print(arr)