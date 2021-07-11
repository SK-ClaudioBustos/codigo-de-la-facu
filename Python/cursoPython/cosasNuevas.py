#funciones lambda

nro = 5;
x = lambda x: x + 5
print(x(nro))

def multi(x):
    return lambda n: n * x

doble = multi(2)
triple = multi(3)
print(doble(7))
print(triple(5))

print((lambda c: c**2 + 5)(-4))


#funcion map

def sumar5(x):
    return x + 5

nums = [12,33,44]
resultado =list(map(sumar5, nums))
print(resultado)


#funcion filter

def filterPairs(x):
    if(x%2 == 0):
        return x
    pass

filtroLambda = list(filter(lambda t: t%2 == 0,nums ))
print(filtroLambda)

filtroFuncion = list(filter(filterPairs,nums))
print(filtroFuncion)


#generadores

def filterGenerator(x):
    for z in range (1,x):
        if(z%2 == 0):
            yield z

print(list(filterGenerator(11)))


#decorators

def decora(priT):
    def wrap():
        print("--------------")
        priT()
        print("--------------")
    return wrap

@decora
def printT():
    print("hola mundo")

decoreted =  decora(printT)
decoreted()
printT()


#exceptions y try
'''
existen distintas excepciones como:
ImportError: falla una importacion
IndexError: cuando se indexa un lista fuera de rango
NameError: una variable desconocida es usada
SyntaxError: error de sintaxis
TypeError: cuando se llama a una funcion con un argumento que es de un tipo invalido
ValueError: cuando se llama a una funcion con un argumento que posee un valor invalido
'''
try:
    num1 = 7
    num2 = 0
    print(num1/num2)
except ZeroDivisionError:
    print("SE ESTA HACIENDO UNA DIVISION POR CERO")
#se puede usar dos except tambien
try:
    num1 = 5
    print(num1/"a")
except ZeroDivisionError:
    print("SE ESTA HACIENDO UNA DIVISION POR CERO")
except (ValueError,TypeError):
    print("OCURRIO UN ERROR")
#en esta caso finally se utiliza para indicar un mensaje que se mostrar al final pase lo que pase
try:
    num3 = 22
    print(num3/0)
except:
    print("OCURRIO UN ERROR DESCONOCIDO")
finally:
    print("esta linea se mostrara sin importar que")
#el else se usa para ejecutar algo extra sino se ejecuta el except
try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)


#raising exceptions

#se podria decir que se usan para invocar un error en el caso que se cumpla una determinada condicion
num = 102
if num >100:
    raise ValueError("debe introducir un valor menor a 100")


#archivos

#modo lectura
file = open("archivo.txt","r")
#modo escritura
file = open("archivo.txt","w")
#modo agregar al final
file = open("archivo.txt","a")
#modo escritura y binario 
file = open("arhcivo.txt","wb")
#modo lectura y binario
file = open("arc.txt","rb")
#para leer un archivo
file = open("/SK/in/tetx.txt")
texto = file.read()
#para leer porciones del contenido,si se llama al file.read() este devolvera el resto del contenido
file.read(4)
file.read(5)
#para leer linea por linea,el metodo readlines() devuelve un lista con el contenido del archivo
for line in file.readlines():
    print(line)
#para escribir archivos
file.write("Nueva linea")
#si se quiere añadir una nueva linea a un archivo existente,se debe agregar un salto de linea
file.write("\nNueva linea")
#el metodo write devuelve el len() de la palabra escrita
texot = "nueva liena"
cant = file.write(texot)
#por ultimo el metodo para cerrar un archivo
file.close()
#hay 2 formas de cerrar un archivo de manera coqueta
try:
    file = open("arhcivo.txt","w")
    file.write("linea 1")
finally:
   file.close()
#lo bueno de este metodo es que se cierra el archivo una vez que se sale del bloque with
with open("arhcivo.txt") as f:
    print(f.read())


#assert

#sirve como comprobacion de validez,en el caso de que no pase el assert,osea de falso
#se mostrara un error
assert 2 + 2 == 4
print("paso el punto 1")
assert 1 + 1 == 3
print("paso al punto 2")
#en este caso se crea un assert personalizado
temp = -10
assert (temp >=0),"esta mas frio que 0 grados"


#all y any

nums = [55, 44, 33, 22, 11]
#en este caso se pregunta si todos los numeros son mayores a 5
if all([i > 5 for i in nums]):
    print("All larger than 5")
#se mostrara el mensaje si por lo menos 1 numero es par
if any([i % 2 == 0 for i in nums]):
    print("At least one is even")
#se enumera los numeros de la lista con sus respectivos indices
for v in enumerate(nums):
    print(v)


#creacion de listas con filtros 

#creo una lista la cual posea nros elevados a la 3
cubes = [i**3 for i in range(5)]
print(cubes)
#se crea una lista con nros cuadrados par
evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)


# modulo itertools

from itertools import count,accumulate,takewhile,product,permutations
#genera nros del 3 hasta que se salga del ciclo for
for i in count(3):
    print(i)
    if i >=11:
        break
#forma los nros con el nro actual del rango mas los anteriores
nums = list(accumulate(range(8)))
print(nums)
#takewhile funciona de la misma manera que filter
print(list(takewhile(lambda x: x<= 6, nums)))
letters = ("A", "B")
#product lo que hace es multiplicar todos los elementos de un conjunto con los de otro
print(list(product(letters, range(2))))
#permutations muestra todas las combinaciones disponibles,importando el orden
print(list(permutations(letters))) 


# del

#se usa para borrar una variable
a = 2
del a 


#expresiones regulares

import re
pattern = r"spam"
#match se usa para verificar si una palabra se encuentra en otra 
if re.match(pattern, "spamspamspam"):
    print("Match")
else:
    print("No match")
if re.match(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")
#search sirve para buscar una palabra en otra 
if re.search(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")
#en esta caso findall muestra todas las coincidencias con la pattern
print(re.findall(pattern, "eggspamsausagespam"))
pattern = r"pam"
match = re.search(pattern, "eggspamsausage")
#group es para mostrar todas las coincidencias,
#start para mostrar la posicion inicial de la primera coincidencia,
#end para mostrar la posicion final de la primera coincidencia,
#spam muestra entre que posiciones esta la primera coincidencia
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
#este metodo lo que hace es reemplazar la palabra indicada con otra
stri = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", stri)
print(newstr)
#esta match verifica si la palabra contiene solo letras,numeros y guiones bajos
if re.match('^[a-zA-Z0-9_]+$', str):
    print("palabra correcta")


#metacaracteres

#basicamente nos permite usar caracteres especiales en los string
palabra = r"tuvieja\r\a\t"
#el punto se usa para decir que cualquier cosa puede ir ahi menos un espacio
pattern = r"gr.y"
if re.match(pattern, "grey"):
    print("Match 1")
if re.match(pattern, "gray"):
    print("Match 2")
if re.match(pattern, "blue"):
    print("Match 3")
#estos signos dicen que debe empezar con gr y terminar con y
pattern = r"^gr.y$"
#caracteres de clases,se verifica si la palabra introducida tiene por lo menos una de las letras de la clase
pattern = r"[aeiou]"
if re.search(pattern, "grey"):
    print("Match 1")
if re.search(pattern, "qwertyuiop"):
    print("Match 2")
if re.search(pattern, "rhythm myths"):
    print("Match 3")
#tambien se puede definir rangos,en este caso debe tener dos mayusculas y un nro al final
pattern = r"[A-Z][A-Z][0-9]"
if re.search(pattern, "LS8"):
    print("Match 1")
if re.search(pattern, "E3"):
    print("Match 2")
if re.search(pattern, "1ab"):
    print("Match 3")
#esto verifica que ninguna palabra debe tener todos las letras en mayuscula
pattern = r"[^A-Z]"
if re.search(pattern, "this is all quiet"):
    print("Match 1")
if re.search(pattern, "AbCdEfG123"):
    print("Match 2")
if re.search(pattern, "THISISALLSHOUTING"):
    print("Match 3")
#el asterisco sirve para definir que la palabra debe empezar con egg 
#y puede seguir con spam 0 veces o mas despues 
pattern = r"egg(spam)*"
if re.match(pattern, "egg"):
    print("Match 1")
if re.match(pattern, "eggspamspamegg"):
    print("Match 2")
if re.match(pattern, "spam"):
    print("Match 3")
#el simbolo + sirve de igual manera que * pero,se debe tener por lo menos una repeticion de lo que se aclara,en este caso g
pattern = r"g+"
if re.match(pattern, "g"):
    print("Match 1")
if re.match(pattern, "gggggggggggggg"):
    print("Match 2")
if re.match(pattern, "abc"):
    print("Match 3")
#el simbolo ? sirve para indicar que se puede repetir el caracter cero veces o una vez
pattern = r"ice(-)?cream"
if re.match(pattern, "ice-cream"):
    print("Match 1")
if re.match(pattern, "icecream"):
    print("Match 2")
if re.match(pattern, "sausages"):
    print("Match 3")
if re.match(pattern, "ice--ice"):
    print("Match 4")
#entre corchetes se indica cuantas veces se puede repetir el caracter
pattern = r"9{1,3}$"
if re.match(pattern, "9"):
    print("Match 1")
if re.match(pattern, "999"):
    print("Match 2")
if re.match(pattern, "9999"):
    print("Match 3")
#los grupos son subconjuntos de metacaracteres,se simbolizan con parentesis
pattern = r"a(bc)(de)(f(g)h)i"
match = re.match(pattern, "abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())
#luego tenemos a los grupos que se pueden identificar con una etiqueta (?P<name>...),
#tambien los grupos que no se puede hacer una referencia directa con group(def) sino que se debe usar group()
pattern = r"(?P<first>abc)(?:def)(ghi)"
match = re.match(pattern, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())
#el simbolo | significa que se usa a o e en la composicion de la palabra
pattern = r"gr(a|e)y"
match = re.match(pattern, "gray")
if match:
    print ("Match 1")
match = re.match(pattern, "grey")
if match:
    print ("Match 2")    
match = re.match(pattern, "griy")
if match:
     print ("Match 3")


#*args,*kwargs

#con args le pasamos varios parametro que se guardan como un tupla
def function(named_arg, *args):
    print(named_arg)
    print(args)
function(1, 2, 3, 4, 5)
#kwargs se usa para pasar argumentos en un diccionario,en este caso el diccionario solo se llena con las claves a y b
def my_func(x, y=7, *args, **kwargs):
    print(kwargs)
my_func(2, 3, 4, 5, 6, a=7, b=8)


#en este caso c toma todos los valores restantes hacia la derecha

a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)


#operador ternario

#se usa cuando resumimos una condicion
a = 7
b = 1 if a >= 5 else 42
print(b)


#usos else

#en est caso saltara con el primer for ya que cuando se usa else el for cambia su naturaleza
#para que no entre en el if es necesario poner un valor menor al rango
for i in range(10):
    if i == 999:
        break
else:
    print("Unbroken 1")
for i in range(10):
    if i == 5:
        break
else:
    print("Unbroken 2")
#el else se ejecuta si se pasa el try
try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)
try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)


#metodos de cadenas

palabra = "aBra"
#este metodo permite que la primera letra de la palabra este en mayusculas y el resto en minusculas
palabra.capitalize()
#este metodo permite que se generen espacio alrededor de la palabra
#en este caso se generaran 2 espacios y 3 espacios luego de la palabra
palabra.center(10)
#en este ejemplo se sustituyen los espacios por asteriscos
palabra.center(10,"*")
#verifica si la palabra termina con el parametro especificado
palabra.endswith("ses")
#devuelve verdadero si la palabra empieza con la cadena especificada
print("omega".startswith("meg"))
print("omega".startswith("om"))
#busca si la palabra contiene la subcadena indicada, sino la encuentra devuelve -1
print("Eta".find("ta"))
#este ejemplo demuestra como se puede mostrar todos los indices de la letra encontrada
txt = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""
fnd = txt.find('the')
while fnd != -1:
    print(fnd)
    fnd = txt.find('the', fnd + 1)
#en esta variante se indica en donde se empieza y en donde no se tomara en cuenta 
#el 1 es donde se empezara el 4 es la posicion donde no se tomara en cuenta 
print('kappa'.find('a', 1, 4))
#lo mismo que find pero comienza desde el final
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))
#devuelve verdadero si la cadena possee solo nros o letra
t = 'Six lambdas'
print(t.isalnum())
t = 'ΑβΓδ'
print(t.isalnum())
t = '20E1'
print(t.isalnum())
#el método isdigit() devuelve true si encuentra dígitos
palabra.isdigit()
#lo mismo que lo anterior pero con letras y caracteres
palabra.isalpha()
#devuelve verdadero si todas las letras estan en minusculas
palabra.islower()
#lo mismo que lo anterior pero si estan en mayusculas
palabra.isupper()
#devuelve true si solo hay espacios en blanco
palabra.isspace()
#recibe una lista que separa con algun caracter especificado
print("mm".join(["omicron", "pi", "rho"]))
#deja todo en minusculas, el contrario de upper
print("SiGmA=60".lower())
#elimina todos los espacios en blanco INICIALES
print("[" + " tau ".lstrip() + "]")
#elimina todos los espacios incluso el parametros especificado
print("www.cisco.com".lstrip("w."))
#variante de lstrip pero toma la parte derecha de la cadena
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))
#combinacion de las dos anteriores
print("[" + "   aleph   ".strip() + "]")
#reemplaza la primera palabra con la segunda
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
#el tercer parametro limita la cantidad de reemplazos
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))
#vuelve todas las mayusculas a minusculas y viceversa
print("Yo sé que no sé nada.".swapcase())
#pone en mayusculas las primeras letras de una palabra
print("Yo sé que no sé nada. Parte 1.".title())



