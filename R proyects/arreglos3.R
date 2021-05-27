#Categorias - funcion factor
animales <- c("tortuga","rana","rana","perro","perro","gato")
#la funcion factor devuelve las categorias que posee el vector
niveles <- factor(animales)
print(niveles)
#con summary se cuenta la cantidad de veces que se repiten las palabras 
cantidad <- summary(factor(animales))
print(cantidad)
#en esta caso ordenaremos un vector que posee palabras que se repiten
temperaturas <- c("soleado","nublado","seminublado","soleado","nublado","nublado")
temperaturas.ordenadas <- factor(temperaturas.ordenadas,ordered = T,levels = c("soleado","nublado","seminublado"))
