def triangulo(a, fila = [], cero = [],  b = 1):
   for n in range(b):
     fila = [1]
     cero = [0]
   if (a == 0):
      fila = [i + d for i, d in zip(fila + cero, cero + fila)]
   else:
      for n in range(b):
         print(fila)
      fila = [d + i for d, i in zip(fila + cero, cero + fila)]
      print(fila)
      triangulo(a-1, fila, cero, b-1)

x = int(input("Ingrese la cantidad de filas: "))
triangulo(x)