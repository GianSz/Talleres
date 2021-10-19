import time
start= time.time()

def listaSinDuplicados(lista):
    listaFinal=[]
    for i in range (0, len(lista)-1):
        if lista[i] not in listaFinal:
            listaFinal.append(lista[i])
    return listaFinal

lista = [4,7,11,4,9,5,11,7,3,5]
print("Lista con duplicados:", lista)
print("\nLista sin duplicados:", listaSinDuplicados(lista))

end = time.time()
print( "\nEl tiempo de ejecución fue:", end - start )