import time
start= time.time()

def listaSinDuplicados(lista):
    listaFinal=[]
    for i in range (0, len(lista)-1):
        if lista[i] not in listaFinal:
            listaFinal.append(lista[i])
    return listaFinal

lista = [3,4,4,5,5,7,7,9,11,11]
print("Lista con duplicados:", lista)
print("\nLista sin duplicados:", listaSinDuplicados(lista))

end = time.time()
print( "\nEl tiempo de ejecución fue:", end - start )