'''Ejercicio 15
Escriba un programa que exhiba en pantalla el siguiente menú:
CALCULOS
A- Calcular el doble del dato.
B- Determinar si es par.
C- Determinar si es primo.
D- Salir.
Elija una Opción (A..DE): _
El programa debe ingresar un dato y presentar el menú. Luego, de acuerdo a la
selección el usuario debe resolver las opciones propuestas en el menú. Además
debe validar la entrada de la opción (A..D) indicando un mensaje de error si
corresponde. Resuelva cada opción del menú con una función creada por Ud.'''


def doble(nro):
    return nro * 2


def par(nro):
    if nro % 2 == 0:
        return True
    else:
        return False


def primo(nro):
    if nro > 1:
        for x in range(2, nro):
            if nro % x == 0:
                return False
    return True


while True:

    z =int(input("Introduzca un entero:  "))

    print("\tA- Calcular el doble del dato.")
    print("\tB- Determinar si es par.")
    print("\tC- Determinar si es primo.")
    print("\tD- Salir.")

    x = str(input("\nIntroduzca una opcion(A,B,C,D):"))

    if x != 'A':
        if x != 'B':
            if x != 'C':
                if x != 'D':
                    x = str(input("INTRODUZCA UN OPCION VALIDA!!!:"))
    if x == 'D':
        print("\tSALIENDO DEL PROGRAMA")
        exit(1)

    switch = {
        "A": doble(z),
        "B": par(z),
        "C": primo(z)
    }
    print("Resultado Obtenido:" + str(switch.get(x)) + "\n\n")
