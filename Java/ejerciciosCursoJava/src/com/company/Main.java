package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        //ejercicios curso:
        //obtener volumen de cubo rectangulo
        int largo = 15;
        int ancho = 23;
        int alto = 12;
        int volumenCuboR = largo * ancho * alto;
        //obtener energia cinetica
        double masa = 12;
        double velocidad = 3;
        double energiaCinetica = (12 * Math.pow(velocidad, 2)) / 2.0;
		/*
		Crea un programa que te pida una cantidad en miligramos para una poción
		multijugos, el valor debe ser de tipo entero, si el valor es mayor a 100 imprime
		“¡Felicidades, es una buena poción!”, de lo contrario imprime “La poción es
		mediocre, sangre sucia inmunda”
		 */
        System.out.print("Introduce la cantidad de miligramos para la pocion multijugos: ");
        Scanner miligramos = new Scanner(System.in);
        int resp = miligramos.nextInt();
        if (resp > 100) {
            System.out.println("¡Felicidades, es una buena poción!");
        } else {
            System.out.println("La poción es mediocre, sangre sucia inmunda");
        }
		/*
		Escribe un programa que te diga si un carro de Uber puede iniciar su recorrido, para
		esto se necesitan dos cosas, que el conductor esté cerca y que esté disponible, el
		programa te pedirá dos valores, la distancia del conductor en kilómetros y su
		disponibilidad, donde false = no disponible y true = disponible, según los datos que
		insertes imprime lo siguiente:
						➢ Si la distancia es menor o igual a 0.5 km y el conductor está disponible,
						imprime “Listo para iniciar recorrido”
						➢ Si la distancia es menor o igual a 0.5 km y el conductor NO está disponible,
						imprime, “Conductor cercano, pero no disponible”
						➢ Si la distancia es mayor a 0.5 km y el conductor está disponible, imprime,
						“Conductor disponible pero muy lejos, aplicarán tarifas más altas”
						➢ Si la distancia es mayor a 0.5 km y el conductor NO está disponible, imprime,
						“No hay conductores disponibles”
		 */
        System.out.print("Introduzca la distancia del conductor en km: ");
        Scanner in1 = new Scanner(System.in);
        double distancia = in1.nextDouble();
        System.out.print("Introduzca el conductor esta disponible(si-no): ");
        Scanner in2 = new Scanner(System.in);
        String disponible = in1.nextLine();
        boolean rpta;
        if (disponible == "si") {
            rpta = true;
        } else {
            rpta = false;
        }
        if (distancia <= 0.5 && rpta) {
            System.out.println("Listo para iniciar recorrido");
        }
        if (distancia <= 0.5 && !rpta) {
            System.out.println("Conductor cercano, pero no disponible");
        }
        if (distancia > 0.5 && rpta) {
            System.out.println("Conductor disponible pero muy lejos, aplicarán tarifas más altas");
        }
        if (distancia > 0.5 && !rpta) {
            System.out.println("No hay conductores disponibles");
        }
        /*
        Haz un ciclo for y while que obtenga la sumatoria de los números hasta n, ejemplo,
        para 5 debes obtener 15 (1+2+3+4+5), para 3 debes obtener 6. Imprime el resultado
        así: “La suma es 15” usando formatos de String
         */
        int valorObtenerSumatoria = 5;
        int cont = 0;
        for (int i = 1; i < valorObtenerSumatoria + 1; i++) {
            cont += i;
        }
        System.out.println("El valor de la sumatoria de " + valorObtenerSumatoria + " es: " + cont);

        /*
        Para un Arreglo de String de títulos de películas, imprime el título de la película con
        el título más largo. Por ejemplo si tenemos un arreglo con los valores:
        {“Jumanji”, “Toy Story”, “Pulp Fiction”, “Batman: El caballero de la noche”, “Kill Bill”}
        Debería imprimir “Batman: El caballero de la noche”.
         */

        String arreglo[] = {"Jumanji", "Toy Story", "Pulp Fiction", "Batman: El caballero de la noche", "Kill Bill"};
        int bigTitle = 0;
        for (String i: arreglo){
            if(i.length() > bigTitle){
                bigTitle = i.length();
            }
        }
        System.out.println("El titulo con mayor tamaño es: " + bigTitle);
        /*
        EJERCICIO RETO SUPER SAYAYÍN:Escribe un programa que para un número N,
        imprima los números pares desde 1 hasta N, por ejemplo si N = 6, debe imprimir “2,
        4, 6”. Hazlo con un for o un while. Si el número es menor o igual a 0, debes imprimir
        “Inserta un número positivo”
         */
        int N = 10;
        for(int i = 2; i < N; i++){
            if(i%2 == 0){
                System.out.println(i);
            }
        }

    }
}
