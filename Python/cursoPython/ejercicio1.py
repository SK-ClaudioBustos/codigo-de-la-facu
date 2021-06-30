
palabra = str(input("Introduzca una palabra: "))
dict =  {}
for x in palabra:
    if(dict.get(x) == None):
        dict[x] = 1
    else:
        dict[x] += 1

print(dict)