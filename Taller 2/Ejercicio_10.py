def busquedaBinaria(lista, item):
    posInicial = 0
    posFinal = len(lista) - 1
    encontrado = False
    
    while posInicial <= posFinal and not encontrado:
        mitad = int((posInicial + posFinal)/2)

        if lista[mitad] == item: 
            encontrado = True

        elif lista[mitad] > item:
            posFinal = mitad - 1
        
        else:
            posInicial = mitad + 1
        

    return encontrado

def buscarEnMatriz(matriz, valor):

    for i in range(0,len(matriz)):

        if(busquedaBinaria(matriz[i], valor)):
            return "sí"
    
    return "no"

matriz = [[1,2,2,2,3,4],[1,2,3,3,4,5],[3,4,4,4,4,6],[4,5,6,7,8,9]]
print(buscarEnMatriz(matriz, 7))