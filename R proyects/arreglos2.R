#Operaciones con filas y columnas en matrices
empresa1 <- c(120,140,69)
empresa2 <- c(334,450,29)
ventasE <- c(empresa1,empresa2)
ventas <- matrix(ventasE,nrow = 2,byrow = T)
meses <- c("enero","febrero","marzo")
nombresE <- c("empresa1","empresa2")
colnames(ventas) <- meses
rownames(ventas) <- nombresE
#con esto le agragamos otra empresa mas
empresa3 <- c(12,44,66)
ventas <-rbind(ventas,empresa3)
print(ventas)
#ahora sumaremos los valores de las columnas
colSums(ventas)
#con este metodo sacamos las medias por empresa
rowMeans(ventas)
#ahora meteremos una nueva columna que tendra los promedios de las empresas
promedios <- rowMeans(ventas)
ventas <- cbind(ventas,promedios)
print(ventas)

#acceder a elementos de una matriz,es [fila,columna]
matriz <- matrix(1:25,byrow = T,nrow = 5)
print(matriz[5,5])
#para seleccionar solo una fila
matriz[1,]
#para una columna
matriz[,2]
#para seleccionar dos columnas
matriz[,1:2]
#si quisieramos las 3 primeras filas
matriz[1:3,]





