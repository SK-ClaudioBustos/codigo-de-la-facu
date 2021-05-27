#Vector
vectorE <- c(1,2,3,4)
vectorS <- c("hola","cesar","maar")
vectorL <- c(TRUE,FALSE,T,F)
#crea un vector que tiene nros del 1 hasta el 10
vect <- 1:10
#en este vector veremos que transforma lo nros en caracteres
vectorMagico <- c(1,2,3,"hola")
#con names se puede asignar nombres a las columnas del vector
vector1 <- c("columna 1","columna 2","columna 3")
vector2 <- c(244,454,174)
names(vector2) <- vector1
print(vector2)
#acceder a elementos de un vector(esto tambien se aplica a los vectores que se crean con names)
vector1[1]
#esto se utiliza para acceder a multiples valores del vector 
vector1[c(2,3)]
#desde la columna 2 hasta la 4
vector1[2:4]
#se acceden a los elementos de un vector segun la condicion
filtro <- vector2 >= 300
print(vector2[filtro])

#Operaciones con vectores
vec1 <- c(1,2,3)
vec2 <- c(4,7,69)
Suma<- vec1 + vec2
Div <- vec1 / vec2
Resta <- vec1 - vec2
#para sumar todos los elementos de un vector
t <- c(4,2,5)
sum(t)
#para saber la media
mean(t)
#calcular desviacion estandar
eje <- c(2,3,5,0,1,4,0,6,2,1,1,0,2,4,5,3,1,2,3,2,3,1,2,4,4,2,5,4,1,3,2,6,8,2,0,1,0,2,3,1,5,10,2,1,3,6,2,0,1,3)
print(sd(eje))
#maximo elemento y minimo
minimo <- min(eje)
maximo <- max(eje)
#se multiplican los elementos de un vector entre si
prod(eje)

#Matrices
ve <- 1:10
matriz1Fila <-matrix(ve)
print(matriz1Fila)
#en esta caso se ordenan los nros por columna
matriz2Filas <- matrix(ve,nrow = 2)
print(matriz2Filas)
#en este caso la matriz se ordena por filas
matriz3 <- matrix(ve,nrow = 2,byrow = TRUE)
print(matriz3)
#ahora crearemos una tabla con datos de empresas
empresa1 <- c(120,140,69)
empresa2 <- c(334,450,29)
ventasE <- c(empresa1,empresa2)
ventas <- matrix(ventasE,nrow = 2,byrow = T)
meses <- c("enero","febrero","marzo")
nombresE <- c("empresa 1","empresa 2")
colnames(ventas) <- meses
rownames(ventas) <- nombresE
print(ventas)

#Operaciones Aritmeticas con matrices
matriz <- matrix(1:16,nrow = 4,byrow = T)
#ahora le sumaremos 4 a cada elemento de la matriz
matriz <- matriz + 4
print(matriz)
matriz <- matriz - 4
matriz <- matriz / 2
matriz <- matriz * 2
matriz <- matriz * matriz
filtro <- matriz >= 100
print(matriz[filtro])

