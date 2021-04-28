package com.company;

import java.util.Random;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		System.out.print("Curso de Java");

		//variables

		String nombre = "claudio";
		String subString = nombre.substring(2, 4);
		String remplazo = nombre.replace("o", "4");

		int entero = 123;
		int tamanio = nombre.length();
		float flotante = 1.3f;
		long enteroL = 3435064213213l;

		boolean x = nombre.contains("c");
		boolean z = nombre.isEmpty();

		System.out.println(String.format("Hola webon con edad = %d  %f", tamanio, flotante));
		//nos da un nro random,tambien funciona con char,boolean,etc.Tambien se le puede poner un limite
		Random nroRandom = new Random();
		int limite = 10;
		int nroR = nroRandom.nextInt(limite);

		//nro elevado al cuadrado
		int nro = 2;
		int exponente = 2;
		double cuadrado = Math.pow(nro, exponente);
		//para que devuelva un int hay que castear
		int cuadrado2 = (int) Math.pow(nro, exponente);


		//arreglos
		int[] vector = new int[5];
		vector[0] = 0;
		vector[1] = 1;
		vector[2] = 2;
		vector[3] = 3;
		vector[4] = 4;
		int[] vec = new int[]{1,2,3,4,5};
		String[] palabras = new String[]{"ttaa","tutu","ehehe"};


		//condicionales,bucles,ciclos
		if (nro == 2) {
			System.out.println("ESTO IMPRIME UN TEXTO Y LUEGO AGREGA UN SALTO DE LINEA");
		} else if (exponente != 2) {
			while (true) {
				System.out.print("ESTO IMPRIME UN TEXTO SIN SALTO DE LINEA");
			}
		}

		for(int j = 0; j<5 ; j++){
			System.out.println("Tu vieja");
		}

		do{
			System.out.print("En los ciclos DO siempre se entra por lo menos una vez");
		}while(nro == 3);

		char letra = 'a';
		switch (letra){
			case 'a':
				System.out.println("LETRA A");
				break;
			case 'b':
				System.out.println("Tengo que usar mas el switch antes que el if");
				break;
			default:
				System.out.println("Tambien tengo que usar el default");
		}

		int cont = 0;
		for (int i : vector){
			cont += i;
		}
		for(String g : palabras){
			if(g.contains("a")){
				System.out.print("esta palabra no tiene a");
			}
		}
		//este bloque de control se usa para capturar errores,es recomendable que el try englobe lo minimo de codigo y que
		//no siempre se tiene que usar el Exception
		try{
			System.out.println("EL PROGRAMA ANDA BIEN");
		}
		catch (Exception e){
			System.out.println("SI EL PROGRAMA DETECTA UN ERROR ,IMPRIMIRA ESTE MENSAJE");
		}

		//entrada de datos
		System.out.print("Introduzca algunos valores: ");
		Scanner input = new Scanner(System.in);
		int ent = input.nextInt();
		float flot = input.nextFloat();
		String cadena = input.nextLine();
		double decimal = input.nextDouble();

	}//fin de main
}//fin de clase main