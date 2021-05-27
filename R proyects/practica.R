#ejercicio 1
ventas <- c(120,140,90)
names(ventas) <- c("enero","febrero","marzo")
media <- mean(ventas)
ventasMay <-ventas[ventas > 100]
ventaMax <- max(ventas)

print(ventas)
print(media)
print(ventasMay)
print(ventaMax)

#ejercicio 2
vector1 <- c(4,10,5,3)
vector2 <- c(2,8,25,14)
matriz <- matrix(c(vector1,vector2),nrow = 2,byrow = T)
print(matriz)

matriz2 <- matrix(c(1:24),nrow = 6,byrow = T)
print(matriz2)
val <- matriz2[3,4]
nueva.matriz <- matriz2[1:3,1:2]
print(nueva.matriz)
nueva.matriz <- cbind(nueva.matriz,rowSums(nueva.matriz))
print(nueva.matriz)

#ejercicio 3
nombres <- c("Antonio","Maria","Juan")
edades <- c(40,30,35)
sexos <- c("M","F","M")
dataFrame <- data.frame(nombres,edades,sexos)
print(dataFrame)
