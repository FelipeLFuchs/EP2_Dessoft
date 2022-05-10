import random
def sorteia_letra(palavra,restritas):
    lista = []
    especiais = ['.', ',', '-', ';', ' ']
    for i in palavra:
        if i not in especiais and i not in restritas:
            lista.append(i)
    return random.choice(lista)