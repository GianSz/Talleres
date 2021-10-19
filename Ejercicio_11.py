def quickSort (arr, left, right):
    if left < right:
        pivotPos = pivot(arr, left, right)
        quickSort(arr, left, pivotPos - 1)
        quickSort(arr, pivotPos + 1, right)

def pivot(arr, left, right):
    i = left
    j = right - 1
    p = arr[right]

    while i < j:

        while i < right and arr[i] < p:            
            i += 1

        while j > left and arr[j] >= p:             
            j -= 1

        if i < j:                                   
            arr[i], arr[j] = arr[j], arr[i]         

    if arr[i] > p:                                
        arr[i], arr[right] = arr[right], arr[i]
    
    return i 

