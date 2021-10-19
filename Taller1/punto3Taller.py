def invertirStr(str, indice = 0):

    if(indice == len(str)-1):
        return(str[indice])
    
    else:
        return(invertirStr(str, indice+1) + str[indice])

str = input("Ingrese el texto que desea invertir: ")

strInv = invertirStr(str)
print("El string invertido es:", strInv)