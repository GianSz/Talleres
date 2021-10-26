def shellSort(arr):
    gap = int(len(arr)/2)

    while gap > 0:
        i = 0
        for posicion in range (gap, len(arr)):
            valorActual = arr[posicion]
            indice = posicion

            while (indice >= gap and arr[indice - gap] > valorActual):
                arr[indice] = arr[indice - gap]
                indice -= gap
        
            arr[indice] = valorActual
            i += 1
            print("Pasada #", i, "->", arr)
        
        gap = int(gap/2)

array = [8, 43, 17, 6, 40, 16, 18, 97, 11, 7]
shellSort(array)
print("\nFinal ->", array)