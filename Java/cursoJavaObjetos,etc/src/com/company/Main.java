package com.company;

public class Main {

    public static void main(String[] args) {

       Movie p1 = new Movie("alien","terror",90);
        p1.setGenero("Terror");
        p1.setName("Alien");
        p1.setDuracion(90);
        //llama a la funcion toString de Movie
        System.out.println(p1);
        //aca se esta usando la interface para capturar todo el contenido de lo que se muestra
        MediaDownloader.descargar(p1.getName(), new MediaDownloader.downloadListener() {
            @Override
            public void onMediaDownloader(String contente) {
                p1.toString();
                p1.setContent(contente);
                System.out.println(contente);
            }
        });
    }
}
