class Persona:
    def __init__(self,n,e,d):
        self.nombre = n
        self.edad = e
        self.dni = d
    def mostrarDatos(self):
        print("nombre:  {}   edad:  {}   dni: {}".format(self.nombre,self.edad,self.dni))

class Empleado(Persona):
    __AtributoPrivado = 0
    def __init__(self,i,s,n,e,d):
        self.id = i
        self.sueldo = s
        super().__init__(n,e,d)
    def mostrarDatos(self):
        print("MOSTRANDO DATOS EMPLEADO")
        super().mostrarDatos()
        print("id:  {}   sueldo:  {}".format(self.id,self.sueldo))

e = Empleado(123123,400.22,"claudio",20,42602340)

#Magic Methods(sobrecarga de operadores)
#hay bastantes operadores que se pueden sobrecargar
'''
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |
'''
class Cuadrado:
    def __init__(self,lado):
        self.lado = lado
    def __add__(self,other):
        return Cuadrado(self.lado + other.lado)
    def __sub__(self, other):
        return Cuadrado(self.lado - other.lado)
    def __mul__(self, other):
        return Cuadrado(self.lado * other.lado)

c1 = Cuadrado(24)
c2 = Cuadrado(4)
c3 = c1 + c2
#print(c3.lado)
'''
__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=
'''
class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)

spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs

'''
__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in
'''
import random

class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]

    def __len__(self):
        return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])


#el metodo __repr__ muestra como se va actualizando el queue
class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)

#se utiliza el metodo new_square para crear un nuevo rectangulo
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())

#ejemplo de un metodo estatico,osea un metodo que no afecta a los atributos de la clase
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)

#metodo que permite verificar la existencia del atributo de un objeto
class ClaseEjemplo:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

objetoEjemplo = ClaseEjemplo(1)
print(objetoEjemplo.a)

if hasattr(objetoEjemplo, 'b'):
    print(objetoEjemplo.b)

#la cadena name permite mostrar el nombre de al clase
type(objetoEjemplo).__name__
ClaseEjemplo.__name__