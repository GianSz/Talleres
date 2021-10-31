# Si dijeran que la lista está necesariamente ordenada entonces se implementaría el siguiente código. La 
# sitaución de peor caso es en la que todos lo elementos de la lista son negativos, teniendo una complejidad de 
# O(n). 

# El tiempo de ejecución es : 0.0007936954498291016
def returnNegativeValuesOrdered(list):
    finalList = []
    for i in range(0, len(list)):
        if(list[i]<0):
            finalList.append(list[i])
        else:
            break
    return finalList

# Por otro lado si dijeran que la lista no está necesariamente ordenada entonces se implementaría el siguiente
# código. La situación de peor caso es la misma que la del caso mejor o caso regular, ya que siempre se 
# recorre el arreglo del principio al final, teniendo como complejidad O(n). 

# El tiempo de ejecución es: 0.0009899139404296875
def returnNegativeValuesDisordered(list):
    finalList = []
    for i in range(0, len(list)):
        if(list[i]<0):
            finalList.append(list[i])
    
    return finalList