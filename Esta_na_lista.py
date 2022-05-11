def esta_na_lista(nome,lista):
    i = 0
    while i < len(lista):
        if nome == lista[i][0]:
            return True
        i += 1
    return False