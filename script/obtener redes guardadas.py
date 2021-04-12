import subprocess
from colorama import Fore,init

init()

def obtenerPerfiles():
    perfiles =  subprocess.run("netsh wlan show profiles",stdout=subprocess.PIPE,shell=True,universal_newlines=True)
    return perfiles.stdout.splitlines()

def obtenerSSID(perfiles):
    puntero = ""
    lista_de_perfiles = []
    final = 9
    indice_guia = len(perfiles) - 10
    final += indice_guia
    for x in range(9,final):
        puntero = perfiles[x]
        lista_de_perfiles.append(puntero[37+2:])
    return lista_de_perfiles

def obtenerPassword(lista_de_perfiles):
    lista_de_contraseñas = []
    puntero = ""
    indice_guia = len(lista_de_perfiles)
    for x in range(0,indice_guia):
        password = subprocess.run("netsh wlan show profile name=\"" + str(lista_de_perfiles[x]) + "\" key=clear",stdout=subprocess.PIPE,shell=True,universal_newlines=True)
        PassWords = password.stdout.splitlines()
        puntero = PassWords[32]
        lista_de_contraseñas.append(puntero[27+2:])
    return lista_de_contraseñas

def Mostrar(listaP,listaC):
    final = len(listaP)
    for x in range(0,final):
        print(Fore.LIGHTYELLOW_EX + "Nombre de Red: " + Fore.YELLOW  + str(listaP[x]) + Fore.LIGHTBLUE_EX + "            Contraseña: " + Fore.BLUE +str(listaC[x]))

if __name__ == '__main__':

    perfiles = obtenerPerfiles()
    lista_de_perfiles = obtenerSSID(perfiles)
    lista_de_contraseñas = obtenerPassword(lista_de_perfiles)
    Mostrar(lista_de_perfiles,lista_de_contraseñas)



