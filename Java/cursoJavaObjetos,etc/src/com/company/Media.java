package com.company;

public class Media {
    private String name;
    private String genero;
    private int duracion;
    private String content = "";

    public Media(String n,String g,int d){
        this.name = n;
        this.genero = g;
        this.duracion = d;
    }
    public Media(){
        this.name = "No title";
        this.duracion = 0;
        this.genero = "No genre";
    }

    @Override
    public String toString (){
        return "Media name " + name + " ,genre " + genero + " ,duration " + duracion;
    }

    public void setContent(String content){
        this.content = content;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }

    public int getDuracion() {
        return duracion;
    }

    public void setDuracion(int duracion) {
        this.duracion = duracion;
    }
}
