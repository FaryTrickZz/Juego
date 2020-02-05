# -*- coding: UTF-8 -*-

from Personaje import Personaje
from Habilidades import Habilidades
from ListaPersonajes import ListaPersonajes
from Jugador import Jugador
import random


qKayn=Habilidades("Corte Segador", 140, 0, 0, 0)
wKayn=Habilidades("Alcance de cuchilla", 270, 0, 0, 0)
eKayn=Habilidades("Paso sombrio", 0, 150, 0, 0)
rKayn=Habilidades("Transgresion de umbral", 350, 300, 0, 1)

qSylas=Habilidades("Azote de cadenas", 100, 0, 0, 0)
wSylas=Habilidades("Matarreyes", 205, 150, 0, 0)
eSylas=Habilidades("Fuga", 220, 0, 0, 0)
rSylas=Habilidades("Usurpacion", 0, 0, 0, 0)

qEkko=Habilidades("Rebobinador de tiempo", 260, 0, 0, 0)
wEkko=Habilidades("Convergencia paralela", 0, 0, 160, 0)
eEkko=Habilidades("Salto de fase", 140, 0, 0, 0)
rEkko=Habilidades("Cronorruptura", 450, 200, 0, 0)


Kayn=Personaje("Kayn", 2500)
Kayn.setHabilidades(qKayn)
Kayn.setHabilidades(wKayn)
Kayn.setHabilidades(eKayn)
Kayn.setHabilidades(rKayn)

Sylas=Personaje("Sylas", 1900)
Sylas.setHabilidades(qSylas)
Sylas.setHabilidades(wSylas)
Sylas.setHabilidades(eSylas)
Sylas.setHabilidades(rSylas)

Ekko=Personaje("Ekko", 2100)
Ekko.setHabilidades(qEkko)
Ekko.setHabilidades(wEkko)
Ekko.setHabilidades(eEkko)
Ekko.setHabilidades(rEkko)

Lista1=ListaPersonajes("Lista Campeones 1")
Lista1.setCampeones(Kayn)
Lista1.setCampeones(Sylas)
Lista1.setCampeones(Ekko)

print("×××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××")
print("×                     Bienvenido!                             ×")
print("×         Identificate para guardar tu puntuacion             ×")
print("×××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××")

nombreplayer1 = raw_input("Nombre: ")

player=Jugador(nombreplayer1, 500, 0)

menu="x"

print("")
print(nombreplayer1)
print("×××××××××××××××××××××××")
print("×      1. Tienda      ×")
print("×      2. Jugar       ×")
print("×      3. Salir       ×")
print("×××××××××××××××××××××××")
print("")
print("")

menu=int(input())

while menu != 3:
    coste1=250
    if menu== 1:
        print("×××××××××××××××××××××××××××××××××××××××××××××××××")
        print("×       Bienvenido a la tienda                  ×")
        print("×       Tienes: " + str(player.getCreditos())+" creditos                    ×")
        print("×                                               ×")
        print("×       Obtencion de campeones:                 ×")
        print("×       1."+    Lista1.getNombre()+ " Coste: "+str(coste1)  +"          ×")
        print("×                                               ×")
        print("××××××××××××××××××××××××××××××××××××××××××××××××××")

        lista=int(input())

        while lista==1 and player.getCreditos()<coste1:
            print("No tienes creditos suficientes")
            lista = int(input())
            print("×××××××××××××××××××××××××××××××××××××××××××××××××")
            print("×       Bienvenido a la tienda                  ×")
            print("×       Tienes: " + str(player.getCreditos()) + " creditos                    ×")
            print("×                                               ×")
            print("×     Obtencion de campeones:                   ×")
            print("×     1." + Lista1.getNombre() + " Coste: " + str(coste1) + "×")
            print("×                                               ×")
            print("××××××××××××××××××××××××××××××××××××××××××××××××××")

        if lista==1:
            obtenciondepersonaje=random.randint(0,2)

            for champs in player.getPersonajes():
                while Lista1.getCampeones()[obtenciondepersonaje] == champs:
                 obtenciondepersonaje = random.randint(0, 2)

            player.setPersonajes(Lista1.getCampeones()[obtenciondepersonaje])

            print("××××××××××××××××××××××××××××××××××××")
            print("Enhorabuena, has obtenido a: "+ player.getPersonajes()[0].getNombre())
            print("××××××××××××××××××××××××××××××××××××")
            player.setCreditos(player.getCreditos()-250)

        print("")
        print(nombreplayer1)
        print("×××××××××××××××××××××××")
        print("×      1. Tienda      ×")
        print("×      2. Jugar       ×")
        print("×      3. Salir       ×")
        print("×××××××××××××××××××××××")
        print("")
        print("")

        menu = int(input())

    elif menu==2:
        #Menu
        print("")
        print("×××××××××××××××××××××××××××××××××××")
        print("×     Personajes disponibles:     ×")
        cont = 0
        for campeones in player.getPersonajes():
            print("×  1. "+ player.getPersonajes()[cont].getNombre()+ "           ")
            cont = cont +1
        print("×××××××××××××××××××××××××××××××××××")
        print("")

        #Eleccion de personaje
        p1=int(input("Elige un personaje"))
        p2=random.randint(0,2)

        #P2 ha de ser diferente a p1
        while p2 == p1:
            p2 = random.randint(0, 2)

        p1=player.getPersonajes()[p1]
        p2=Lista1.getCampeones()[p2]

        print("Has elegido a "+ p1.getNombre())
        print("Vas a pelear contra "+ p2.getNombre())

        #Turnos de los personajes
        Turnop1 = 0
        Turnop2 = 0
        habilidadp1 = 0
        habilidadp2 = 0

        #Si la vida de un pj llega a 0 se acaba el combate
        while  p1.getHp() > 0 and p2.getHp() > 0:


            #Grafica de los personajes
            print("")
            print("  ××××××××××××××××××××××××××××××××××××××  ")
            print("                  "+ p1.getNombre())
            print("                  "+ str(p1.getHp()))
            print("  ×××××××××××__     ______  ××××××××××××  ")
            print("             \ \   / / ___|               ")
            print("              \ \ / /\___ \               ")
            print("               \ V /  ___) |              ")
            print("  ××××××××××××× \_/  |____/ ××××××××××××  ")
            print("                  " + str(p2.getHp()))
            print("                  " + p2.getNombre())
            print("  ××××××××××××××××××××××××××××××××××××××  ")
            print("")
            turno = 0

            if p2.getHabilidades()[habilidadp2].getStun()==0:

                #Eleccion de habilidad P1
                x=0
                for h in p1.getHabilidades():
                    print (str(x)+" "+h.getSkillname()+ " /Damage: "+str(h.getDamage())+" /Health: "+str(h.getHealth())+" /Shield: "+str(h.getShield()))
                    x=x+1
                habilidadp1 = int(input("Elige una habilidad: "))

                #Comprobacion de turno para la Ultimate
                while habilidadp1 == 3 and  Turnop1 < 4:
                    habilidadp1 = int(input("Elige otra habilidad: "))

                #Comprueba la habilidad elegida
                if habilidadp1 == 0:
                    p1.getHabilidades()[habilidadp1].qSkill(p1.getNombre())
                elif habilidadp1 == 1:
                    p1.getHabilidades()[habilidadp1].wSkill(p1.getNombre())
                elif habilidadp1 == 2:
                    p1.getHabilidades()[habilidadp1].eSkill(p1.getNombre())
                elif habilidadp1 == 3:
                    p1.getHabilidades()[habilidadp1].rSkill(p1.getNombre(), p2)
                    Turnop1=0

                #Comprueba si la habilidad estunea
                if p1.getHabilidades()[habilidadp1].getStun == 1:
                    Stun = 1

                #Comprueba si la habilidad cura
                if p1.getHabilidades()[habilidadp1].getHealth() > 0:
                    p1.getHealth(p1.getHabilidades()[habilidadp1].getHealth())

                # Comprueba si la habilidad proporciona escudo
                if p1.getHabilidades()[habilidadp1].getShield() > 0:
                    p1.getHealth(p1.getHabilidades()[habilidadp1].getShield())

                #Restar vida al oponente
                p2.restarVida(p1.getHabilidades()[habilidadp1].getDamage())

            else:
                print(p1.getNombre()+ " no puede atacar en esta ronda.")
                p2.getHabilidades()[habilidadp1].setStun(0)


            if p1.getHabilidades()[habilidadp1].getStun()==0:

                #Eleccion de habilidad P2
                x = 0
                for h in p2.getHabilidades():
                    x = x + 1

                habilidadp2 = random.randint(0,3)

                # Comprobacion de turno para la Ultimate
                while habilidadp2 == 3 and Turnop1 < 4:
                    habilidadp2 = random.randint(0, 2)

                # Comprueba la habilidad elegida
                if habilidadp1 == 0:
                    p2.getHabilidades()[habilidadp2].qSkill(p2.getNombre())
                elif habilidadp1 == 1:
                    p2.getHabilidades()[habilidadp2].wSkill(p2.getNombre())
                elif habilidadp1 == 2:
                    p2.getHabilidades()[habilidadp2].eSkill(p2.getNombre)
                elif habilidadp1 == 3:
                    p2.getHabilidades()[habilidadp2].qSkill(p2.getNombre(), p1)
                    Turnop2=0

                # Comprueba si la habilidad cura
                if p2.getHabilidades()[habilidadp2].getHealth() > 0:
                    p2.getHealth(p2.getHabilidades()[habilidadp2].getHealth())

                # Comprueba si la habilidad proporciona escudo
                if p2.getHabilidades()[habilidadp2].getShield() > 0:
                    p2.getHealth(p2.getHabilidades()[habilidadp2].getShield())

                #Restar vida al oponente
                p1.restarVida(p2.getHabilidades()[habilidadp2].getDamage())

                #Si un jugador ha utilizado la Ultimate, reinicia los turnos, sino los aumenta
                if habilidadp1 == 3:
                    Turnop1 = 0
                else:
                    Turnop1 = Turnop1+1

                if habilidadp2 == 3:
                    Turnop2 = 0
                else:
                    Turnop2 = Turnop2+1

            else:
                print(p2.getNombre()+ " no puede atacar en esta ronda.")
                p1.getHabilidades()[habilidadp1].setStun(0)

        #Final del combate
        if p1.getHp() <= 0:
            print(p2.getNombre()+" ha ganado.")
            print("Enhorabuena")

        if p2.getHp() <= 0:
           print(p1.getNombre()+" ha ganado.")
           print("Enhorabuena")

        print("")
        print(nombreplayer1)
        print("×××××××××××××××××××××××")
        print("×      1. Tienda      ×")
        print("×      2. Jugar       ×")
        print("×      3. Salir       ×")
        print("×××××××××××××××××××××××")
        print("")
        print("")

        menu = int(input())
