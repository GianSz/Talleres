def invertirNumero(num, indice = 0):

    if(indice == len(num)-1):
        return(num[indice])
    
    else:
        return(invertirNumero(num, indice+1) + num[indice])

numero = input("Ingrese el número que desea invertir: ")

numInv = invertirNumero(numero)
print("El número invertido es:", numInv)