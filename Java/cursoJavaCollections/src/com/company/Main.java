package com.company;
import java.util.*;

public class Main {

    public static void main(String[] args) {
		//JAVA COLLECTIONS FRAMEWORK

		//ArrayList
		ArrayList<String> stringList1 = new ArrayList<>();
		ArrayList<String> stringList2 = new ArrayList<>();
		ArrayList<Integer> integerList = new ArrayList<>();
		ArrayList<Boolean> booleanList = new ArrayList<>();
		//si se hace ctrl + click sobre add,nos dara la descripcion del metodo
		stringList1.add("chirou");
		stringList1.add("cesar");
		stringList1.add("claudio");
		stringList1.remove("cesar");

		boolean contiene = stringList1.contains("claudio");
		int tamanio = stringList1.size();
		stringList2.addAll(stringList1);
		stringList2.add("elias");
		stringList2.add("marcos");
		stringList2.add("kevin");
		stringList2.add("milton");

		//iterar sobre ArrayList
		for (int i = 0; i < stringList2.size(); i++) {
			String elemento = stringList2.get(i);
			System.out.println("Elemento " + i + ": " + elemento);
		}

		for (String indice : stringList2) {
			System.out.println(indice);
		}

		//PriorityQueue
		PriorityQueue<String> stringPriorityQueueQueue = new PriorityQueue<>();
		stringPriorityQueueQueue.add("m4a1");
		stringPriorityQueueQueue.add("ak47");
		stringPriorityQueueQueue.add("benelli m3");
		stringPriorityQueueQueue.add("desert eagle");
		stringPriorityQueueQueue.add("beretta m92");

		//HashMap
		HashMap<String,Integer> hm1 = new HashMap<>();
		hm1.put("clave 1",666);
		hm1.put("clave 2",11);
		hm1.put("clave 3",44);
		hm1.put("clave 4",5151);
	}
}
