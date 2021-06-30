#Ejercicio 20-Realice un programa que pida una letra y detecte si es una vocal.

def vocal(letra):
    if (letra == "a"):
        return True
    if (letra == "e"):
        return True
    if (letra == "i"):
        return True
    if (letra == "o"):
        return True
    if (letra == "u"):
        return True
    return False

if(vocal("g")):
    print("Es una Vocal")
else:
    print("No es una Vocal")