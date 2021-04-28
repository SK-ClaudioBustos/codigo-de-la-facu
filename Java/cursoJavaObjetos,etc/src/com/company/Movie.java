package com.company;

public class Movie extends Media{

    private boolean ganoOscar;

    public Movie(String nombre,String genero,int duracion){
        super(nombre,genero,duracion);
    }

    public Movie(){
        super("","",0);
        this.ganoOscar = false;
    }

    public boolean isGanoOscar() {
        return ganoOscar;
    }

    public void setGanoOscar(boolean ganoOscar) {
        this.ganoOscar = ganoOscar;
    }
}
