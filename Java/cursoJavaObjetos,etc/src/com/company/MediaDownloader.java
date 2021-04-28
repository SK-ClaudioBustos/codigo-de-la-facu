package com.company;

public class MediaDownloader {
    public interface downloadListener{
        void onMediaDownloader(String contente);
    }

    //el metodo runnable sirve para crear un hilo o un proceso paralelo al programa,el thread.sleep lo unico que hace es que se tarde un tiempo
    //en descargar la pelicula
    public static void descargar(String name,downloadListener DL ){
        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                System.out.println("Descargando el titulo: " + name);
                try {
                    Thread.sleep(5000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("Ya se descargo el titulo: " + name);
                String content = "Disfrute de su pelicula o serie";
                DL.onMediaDownloader(content);
            }

        });
        thread.start();
    }


}
