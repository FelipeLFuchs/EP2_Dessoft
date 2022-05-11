def adiciona_em_ordem(pais,distância,lista):
    i=0
    d=0
    c=len(lista)-1
    if len(lista)==0:
        lista.append([pais,distância])
    if pais in lista:
        return lista
    if distância > lista[c][1]:
        lista.insert(len(lista),[pais,distância])
        d=len(lista)
    else:
        while d<len(lista):
            if distância > lista[d][1]:
                i+=1 
            if distância <lista[d][1]:
                lista.insert(i,[pais,distância])
                d=len(lista)
            d+=1
    return lista
