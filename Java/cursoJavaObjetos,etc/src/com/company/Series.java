package com.company;

public class Series extends Media {
    private int episodios;
    private int duracionEpisodios;
    private int temporadas;

    public Series(String nombre,String genero,int duracion,int cantEpisodios,int cantTemporadas){
        super(nombre,genero,duracion);
        this.episodios = cantEpisodios;
        this.duracionEpisodios = duracion;
        this.temporadas = cantTemporadas;
    }

    public Series(){
        super("","",0);
        this.episodios = 0;
        this.duracionEpisodios = 0;
        this.temporadas = 0;
    }

    public int getEpisodios() { return episodios;  }

    public void setEpisodios(int episodios) {
        this.episodios = episodios;
    }

    @Override
    public int getDuracion() {
        return this.episodios * this.duracionEpisodios;
    }

    public void setDuracionEpisodios(int duracionEpisodios) {
        this.duracionEpisodios = duracionEpisodios;
    }

    public int getTemporadas() {
        return temporadas;
    }

    public void setTemporadas(int temporadas) {
        this.temporadas = temporadas;
    }
}
