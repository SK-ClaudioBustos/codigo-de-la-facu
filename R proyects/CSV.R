#creo un arreglo con nros del 1 al 10
numeros <- 1:10
#creo un arreglo con las primeras 10 letras del abecedario
letras <- letters[1:10]
#creo un data frame
datos <- data.frame(col1 = numeros, col2 = letras)
#ahora creo el fichero CSV
write.csv(datos,file = "fichero.csv")
#asi recuperamos los datos del fichero
datos2 <- read.csv("fichero.csv")
print(datos2)
#para borrar una columna en este caso columna X
datos2$X <- NULL
print(datos2)
