'''
FizzBuzz es una tarea de programación muy conocida, preguntada durante las entrevistas de trabajo. 
 
El código dado resuelve el problema de FizzBuzz y utiliza las palabras "Solo" y "Learn"
en lugar de "Fizz" y "Buzz". 
Toma una entrada n y saca los números de 1 a n. 
Por cada múltiplo de 3, imprime "Solo" en lugar del número. 
Por cada múltiplo de 5, imprime "Learn" en lugar del número. 
Para los números que son múltiplos de 3 y 5, saca "SoloLearn". 
 
Es necesario cambiar el código para saltar los números pares, para que la 
lógica sólo se aplique a los números impares en el rango.
'''

def FizzBuzz(n):
    p1 = "Solo"
    p2 = "Learn"

    for i in range(1,n,2):
        if i%3 == 0 and i%5==0:
            print(p1 + p2)
            continue
        elif i%3 == 0:
            print(p1)
            continue
        elif i%5==0:
            print(p2)
            continue
        else:
            print(i)

FizzBuzz(16)

