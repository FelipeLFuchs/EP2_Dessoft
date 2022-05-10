def normaliza(a):
    s={}
    for cont,pais in a.items():
        for pais, info in a[cont].items():
            info["continente"]=cont
            s[pais]=info
    return s