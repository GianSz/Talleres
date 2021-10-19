def imprimirPalabra(palabra, contador):

    if contador == 0:
        print(palabra[contador])

    else:
        imprimirPalabra(palabra, contador-1)
        print(palabra[0:contador+1])

palabra = input("Escribe una palabra, luego esta será imprimida letra por letra: ")
ultIndice = len(palabra)-1

print("El resultado es el siguiente: ")
imprimirPalabra(palabra, ultIndice)