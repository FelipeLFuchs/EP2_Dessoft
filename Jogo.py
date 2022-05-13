import math
import Lista
from Lista import DADOS
from Lista import EARTH_RADIUS
from sorteando_países import sorteia_pais
from Normalizando_base_de_dados import normaliza
from Adicionando_em_uma_Lista_Ordenada import adiciona_em_ordem
from Distância_de_Haversine import haversine
import Esta_na_lista
import sorteia_com_restrição
class bcolors:   
    RED = "\033[1;91m" 
    BLUE = "\033[1;34m" 
    CYAN = "\033[1;36m" 
    GREEN = "\033[1;92m"
    GREENBR="\033[1;32m"
    GRAY = "\033[1;90m"
    YELLOW = "\033[1;93m"
    YELLOWBR = "\033[1;33m"
    MAGENTA = "\033[1;95m"
    RESET="\033[0m"
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
print("Lista   ----   exibe todos os países possíveis")
final=0
while final==0:       #iniciando o jogo
    tentativas=0      #parâmetros
    faltam=20
    print("                                       ")
    print("                                       ")
    print("Um país foi escolhido, tente adivinhar qual é!!")  
    print("Você tem {0} tentativa(s)".format(faltam))
    Normalizada=(normaliza(DADOS))
    sorteado=(sorteia_pais(Normalizada))
    latitudesort=Normalizada[sorteado]["geo"]["latitude"]
    longitudesort=Normalizada[sorteado]["geo"]["longitude"]
    lista = []
    acerto=0
    pop = 0
    area = 0
    cont = 0
    stri='0'
    valid=["3","4","5"]
    listdicas=[]
    Ordem_alfabética=""
    l = []
    for pais in Normalizada:         #lista de países
        l.append(pais)
    Ordem=(sorted(l))

    for letras in Ordem:
        Ordem_alfabética+=letras
        if letras != "zimbabue":
            Ordem_alfabética+=", "
        if letras == "zimbabue":
            Ordem_alfabética+=". "  



    while tentativas<20:           #TENTATIVAS
        print("")
        chuten=input("Qual seu palpite  ")
        chute=chuten.lower()
        
        if chute=="lista" or chute=="Lista":      #printar lista
            print(Ordem_alfabética)



        if chute in l and chute != sorteado:                            #CHUTA EM PAÍSES
            latitudech=Normalizada[chute]["geo"]["latitude"]
            longitudech=Normalizada[chute]["geo"]["longitude"]
            distancia= (haversine(EARTH_RADIUS, latitudesort, longitudesort, latitudech, longitudech))
            inteiro=int(distancia)+1
            if (inteiro-distancia)<0.50:
                distanciar = (int(distancia)+1)
            else:
                distanciar = (int(distancia))
            lista = (adiciona_em_ordem(chute, distanciar,lista))



            y=0                                                     #DISTÂNCIA E CORES
            indidica=0
            print("Distâncias:")
            print("")
            while y < len(lista):
                if lista [y][0]!= "brasil":
                    if lista[y][1] <=500:
                        print((bcolors.CYAN+'{0} Km -> {1}'+bcolors.RESET).format(lista[y][1],lista[y][0]))
                    if lista[y][1] > 500 and lista[y][1] <= 1000:
                        print((bcolors.GREEN +'{0} Km -> {1}'+bcolors.RESET).format(lista[y][1],lista[y][0]))
                    if lista[y][1] > 1000 and lista[y][1] <= 2000:
                        print((bcolors.YELLOW +'{0:.3f} Km -> {1}'+bcolors.RESET).format(lista[y][1]/1000,lista[y][0]))
                    if lista[y][1] > 2000 and lista[y][1] <= 5000:
                        print((bcolors.MAGENTA +'{0:.3f} Km -> {1}'+bcolors.RESET).format(lista[y][1]/1000,lista[y][0]))
                    if lista[y][1] > 5000 and lista[y][1] <= 10000:
                        print((bcolors.RED +'{0:.3f} Km -> {1}'+bcolors.RESET).format(lista[y][1]/1000,lista[y][0]))
                    if lista[y][1] > 10000:
                        print((bcolors.GRAY +'{0:.3f} Km -> {1}'+bcolors.RESET).format(lista[y][1]/1000,lista[y][0]))
                    
                    y +=1
                if lista [y][0]== "brasil":                             #Brasillllllll
                    if lista[y][1] <=500:
                        print((bcolors.CYAN+"{0} Km ->"+bcolors.YELLOWBR+"{1}"+bcolors.BLUE+"{2}"+bcolors.GREENBR+"{3}"+bcolors.RESET).format(lista[y][1],lista[y][0][0:2],lista[y][0][2:4],lista[y][0][4:6]))
                    if lista[y][1] > 500 and lista[y][1] <= 1000:
                        print((bcolors.GREEN+"{0} Km ->"+bcolors.YELLOWBR+"{1}"+bcolors.BLUE+"{2}"+bcolors.GREENBR+"{3}"+bcolors.RESET).format(lista[y][1],lista[y][0][0:2],lista[y][0][2:4],lista[y][0][4:6]))
                    if lista[y][1] > 1000 and lista[y][1] <= 2000:
                        print((bcolors.YELLOW+"{0:.3f} Km ->"+bcolors.YELLOWBR+"{1}"+bcolors.BLUE+"{2}"+bcolors.GREENBR+"{3}"+bcolors.RESET).format(lista[y][1]/1000,lista[y][0][0:2],lista[y][0][2:4],lista[y][0][4:6]))
                    if lista[y][1] > 2000 and lista[y][1] <= 5000:
                        print((bcolors.MAGENTA+"{0:.3f} Km ->"+bcolors.YELLOWBR+"{1}"+bcolors.BLUE+"{2}"+bcolors.GREENBR+"{3}"+bcolors.RESET).format(lista[y][1]/1000,lista[y][0][0:2],lista[y][0][2:4],lista[y][0][4:6]))
                    if lista[y][1] > 5000 and lista[y][1] <= 10000:
                        print((bcolors.RED+"{0:.3f} Km ->"+bcolors.YELLOWBR+"{1}"+bcolors.BLUE+"{2}"+bcolors.GREENBR+"{3}"+bcolors.RESET).format(lista[y][1]/1000,lista[y][0][0:2],lista[y][0][2:4],lista[y][0][4:6]))
                    if lista[y][1] > 10000:
                        print((bcolors.GRAY+"{0:.3f} Km ->"+bcolors.YELLOWBR+"{1}"+bcolors.BLUE+"{2}"+bcolors.GREENBR+"{3}"+bcolors.RESET).format(lista[y][1]/1000,lista[y][0][0:2],lista[y][0][2:4],lista[y][0][4:6]))
                    
                    y +=1
            tentativas+=1
            print("")
            print("Dicas:")
            while indidica<len(listdicas):
                print(listdicas[indidica])
                indidica+=1
            print("")
            faltam=20-tentativas
            print("Você tem {0} tentativa(s)".format(faltam))        
            



        if chute == 'dica':          #DICA
            if tentativas >= 14:
                if area==0:
                    valid.remove('3')
                area += 1
            if tentativas >= 15:
                if pop==0:
                    valid.remove('4')
                pop += 1
            if tentativas >= 13:
                if cont==0:
                    valid.remove('5')
                cont += 1
            print ('----------------------------------------')
            if tentativas<16:
                print ('1. Cor da bandeira  - custa 4 tentativas')
                stri+='|1'
            if tentativas<17: 
                print ('2. Letra da capital - custa 3 tentativas')
                stri+='|2'
            if tentativas<14 and area==0:
                print ('3. Área             - custa 6 tentativas')
                stri+='|3'
            if tentativas<15 and pop==0:
                print ('4. População        - custa 5 tentativas')
                stri+='|4'
            if tentativas<13 and cont==0:
                print ('5. Continente       - custa 7 tentativas')
                stri+='|5'
            if tentativas<19:
                print ('0. Sem dica                             ')
            print ('----------------------------------------')
            
            solicita =input('Escolha a sua opção [{0}] : '.format(stri))
            if solicita=="3"or solicita=="4" or solicita=="5":
                if solicita not in valid:
                    print("Opção Inválida")
                if solicita in valid:
                    valid.remove(solicita)
                    if solicita=="3":
                        area+=1
                        tentativas+=6
                    if solicita=="4":
                        pop+=1
                        tentativas+=5
                    if solicita=="5":
                        cont+=1
                        tentativas+=7
            stri="0"



        if chute == sorteado:          #ACERTOU
            tentativas+=1
            print("")
            print("***Parabéns meu consagrado, parece que temos um Sherlock Holmes aqui!!!***")
            print("você acertou após {0} tentativas".format(tentativas))
            acerto+=1
            print("")
            b=input("Quer jogar novamente?[s|n]")
            if b=="n":
                final+=1
                tentativas=20
                print("Até a próxima!!!!")

            if b =="s":
                final=0
                tentativas=21



        if chute=="desisto":    
            print("")                               #desisto
            desistir=input("tem certeza que vai desistir??[s|n]")
            if desistir == "s":
                tentativas=20
                acerto+=1
                print("")
                print("Não aguentou a pressão??? O país era {0}".format(sorteado))
                novamente=input("Quer jogar novamente?[s|n]")
                print("")
                print("Até a próxima!!!!")
                final+=1
            if desistir=="n":
                print("")
                print("Você ainda tem {0} tentativa(s)".format(faltam))


        if tentativas>=20 and acerto ==0:               #ERROU
            print("")
            print("Dormiu nas aulas de geografia? O país escolhido era {0}".format(sorteado))
            print("")
            b=input("Quer jogar novamente?[s|n]")
            if b=="s":
                tentativa=20
            
            if b=="n":
                print("")
                print("Até a próxima!!!!")
                final+=1
                    

        if chute not in l and chute != "dica" and chute != "desisto" and chute != "lista":          #desconhecido
            print("")
            print("País não reconhecido, tente novamente")

final=0
    
