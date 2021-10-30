def elecciones(list):
    matriz = [[],[]]

    for i in range(0, len(list)):

        if list[i] not in matriz[0]:
            matriz[0].append(list[i])
            matriz[1].append(1)
        else:
            index = matriz[0].index(list[i])
            matriz[1][index] += 1
    
    ganador = matriz[0][0]
    votosGanador = matriz[1][0]

    for i in range(1, len(matriz[1])):
        if votosGanador < matriz[1][i]:
            votosGanador = matriz[1][i]
            ganador = matriz[0][i]
    
    return ganador