
def mergeSort(arr):

    print("Pasada ->", arr)

    if len(arr) == 1:
        return arr
    
    else:
        arrIzquierda = arr[: len(arr)//2]
        arrDerecha = arr [len(arr)//2 :]

        mergeSort(arrIzquierda)
        mergeSort(arrDerecha)

        posIzq = 0
        posDer = 0
        posArr = 0

        while posIzq < len(arrIzquierda) and posDer < len(arrDerecha):
            
            if arrIzquierda[posIzq] < arrDerecha[posDer]:
                arr[posArr] = arrIzquierda[posIzq]
                posIzq += 1
            
            else:
                arr[posArr] = arrDerecha[posDer]
                posDer += 1

            posArr += 1

        while posIzq < len(arrIzquierda):                                         
            arr[posArr] = arrIzquierda[posIzq]  
            posIzq += 1
            posArr += 1

        while posDer < len(arrDerecha):
            arr[posArr] = arrDerecha[posDer]
            posDer += 1
            posArr += 1

array = [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40] 
mergeSort(array)
print("\nFinal ->", array)