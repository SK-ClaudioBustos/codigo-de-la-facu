def spell1(txt,tam,indice):
    if indice == tam:
        return
    else:
        return print(str(spell1(txt,tam,indice+1)) + "\r" + txt[indice])


#txt = str(input("Introduzca un palabra: "))
#spell1(txt,len(txt),0)

def spell(txt,tam,indice):
    if indice == tam:
        return
    else:
        return print(str(spell(txt,tam,indice+1)).replace("None","") + txt[indice])

txt = str(input("Introduzca un palabra: "))
spell(txt,len(txt),0)