import math
import Lista
from Lista import DADOS
from Lista import EARTH_RADIUS
from sorteando_países import sorteia_pais
from Normalizando_base_de_dados import normaliza
import Adicionando_em_uma_Lista_Ordenada
from Distância_de_Haversine import haversine
import Esta_na_lista
import sorteia_com_restrição
print("=======================================")
print("|                                     |")
print("|    Bem vindo ao jogo dos países     |")
print("|                                     |")
print("|    ==== Design de Software ====     |")
print("|                                     |")
print("|     Feito por Renato.P e Felipe.F   |")
print("=======================================")
print("                                       ")
print("Comandos Básicos:                      ")
print("dica         ----   entra no mercado de dicas")
print("Desisto      ----   desiste da rodada")
print("Inventário   ----   exibe sua posição")
print("                                       ")
print("                                       ")
print("Um país foi escolhido, tente adivinhar qual é!!")
Normalizada=(normaliza(DADOS))
#sorteado=(sorteia_pais(Normalizada))
sorteado='bahamas'
latitudesort=Normalizada[sorteado]["geo"]["latitude"]
longitudesort=Normalizada[sorteado]["geo"]["longitude"]
tentativas=0
while tentativas<20:
    chuten=input("Qual seu palpite  ")
    chute=chuten.lower()
    l = []
    for pais in Normalizada:
        l.append(pais)
    if chute not in l:
        print("País desconhecido")
    else:
        latitudech=Normalizada[chute]["geo"]["latitude"]
        longitudech=Normalizada[chute]["geo"]["longitude"]
        distancia= (haversine(EARTH_RADIUS, latitudesort, longitudesort, latitudech, longitudech))
        inteiro=int(distancia)+1
        if (inteiro-distancia)<0.50:
            print (int(distancia)+1)
        else:
            print(int(distancia))


