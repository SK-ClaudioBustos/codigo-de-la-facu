#include <iostream>
using namespace std;

/*
//usos de namespace
namespace Seccion1{

int suma(int a , int b){
    cout << "int" << endl;
    return a + b;
}

float suma(float a,float b){
    cout << "float" << endl;
    return a + b;
}

double suma(double a,double b){
    cout << "double" << endl;
    return a + b;
}

float resta(float a,float b){
    return a - b;
}
}

//funciones plantilla
template <typename tipo> tipo suma(tipo a,tipo b)
{
    return a + b;
}

//sobrecarga de operadores
struct Punto{
    int x;
    int y;
};

Punto operator+(Punto &a,Punto &b){
    Punto r;
    r.x = a.x + b.x;
    r.y = a.y + b.y;
    return r;
}

Punto operator-(Punto &a,Punto &b);
Punto operator*(Punto &a,Punto &b);

//funciones miembro en struct
//el const se pone porque la funcion no modifica a los valores del struct
struct Persona{
    string nombre;
    string apellido;
    int dni;
    void mostrarDatos()const;
};

void Persona::mostrarDatos()const
{
    cout << nombre << endl;
    cout << apellido << endl;
    cout << dni << endl;
    cout << endl;
}
*/


int main()
{
    /*
    //muestra toda la cadena introducida
    char nombre[50],apellido1[50],apellido2[50];
    cout<<"Introduce tu nombre,primer apellido,segundo apellido";
    cin >> nombre >> apellido1 >> apellido2;
    cout << nombre << " " << apellido1 << " " << apellido2 ;

    //muestra false o true en vez de 1 o 0
    cout << std::boolalpha;
    cout << false << endl;

    //usos de NAMESPACE
    cout << Seccion1::suma(12,3) << endl;
    cout << Seccion1::resta(42,11) << endl;

    //sobre carga de funciones
    cout << Seccion1::suma(1,4) << endl;
    cout << Seccion1::suma(12.2f,32.4f) << endl;
    cout << Seccion1::suma(12.5,3.5) << endl;

    //sobrecarga de operadores
    Punto a , b;
    a.x = 12; a.y = 4;
    b.x = 44; b.y = 6;

    Punto r =  a + b;
    cout << r.x <<"  " << r.y << endl;

    Persona p;
    p.nombre = "claudio";
    p.apellido = "bustos";
    p.dni = 32155124;
    p.mostrarDatos();
    */


    return 0;
}

