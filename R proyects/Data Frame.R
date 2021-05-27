#Data Frame
meses <- c("enero","febrero","marzo")
ventas <- c(124,200,90)
objetivos <- c(T,T,F)

datos <- data.frame(meses,ventas,objetivos)
print(datos)

#para obtener datos del data frame se utiliza
print(str(datos))
print(summary(datos))

#seleccionar datos de un data frame,es como seleccionar filas y columnas en una matriz
print(datos[1,])
print(datos[1:3,1])
print(datos[1,"ventas"])
print(datos[c("ventas","objetivos")])

#tambien se puede seleccionar un conjunto de datos en especifico
subset(datos,subset = ventas >= 100)

#para ordenar los datos en un Data Frame,se utiliza order y se especifica el orden,lo que muestra son los indices
datos <- order(datos,"ventas")
orden.descendiante <- order(-datos,ventas)

#operaciones filas
numeros <- 1:10
letras <- letters[1:10]
dataF1 <- data.frame(numeros,letras)
dataF2 <- data.frame(numeros = 11,letras = "k")
#ahora juntaremos los data frame
dataF3 <- rbind(dataF1,dataF2)
print(dataF3)

#operaciones columnas
numeros <- 1:10
letras <- letters[1:10]
data <- data.frame(col1 = numeros,col2 = letras)
#para crear una nueva columna
data$col3 <- data$col1 *2
print(data)

#para obtener los nombre de las columnas
colnames(data)
#para cambiarlos
colnames(data) <- c
#para cambiarle el nombre a una columna en especifico
colnames(data)[3] <- "Nueva"
#para seleccionar las filas que posean un nro mayor a 3 
columnasM <- data[data$col1 > 3,]


