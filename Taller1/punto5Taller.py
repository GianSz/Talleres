#Método que verifica si una palabra es o no palindromo
def palindromo(str  , contador = 0):

    if contador == len(str) - 1:        #ana
        return str[contador]

    else:
        palabra2 = (palindromo(str, contador + 1) + str[contador])

        if(contador==0):
            if(palabra2 == str):
                return True
            else:
                return False

        return palabra2

str = input("A continuación deberás escribir una palabra, esta seguirá un proceso que verificará si una palabra es palindroma o no lo es. Lo mismo con los números a diferencia que se verificará si es capicúa o no: ")
str = str.upper()

if(palindromo(str)):

    try:
        int(str)
        print("El número es capicúa.")
    except(ValueError):
        print("La palabra es palindroma.")
else:
    try:
        int(str)
        print("El número no es capicúa.")
    except(ValueError):
        print("La palabra no es palindroma.")