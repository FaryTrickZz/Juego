from Personaje import Personaje
from Habilidades import Habilidades
import random


qKayn=Habilidades("Corte Segador", 140, 0, 0)
wKayn=Habilidades("Alcance de cuchilla", 270, 0, 0)
eKayn=Habilidades("Paso sombrio", 0, 150, 0)
rKayn=Habilidades("Transgresion de umbral", 350, 300, 0)

qSylas=Habilidades("Azote de cadenas", 100, 0, 0)
wSylas=Habilidades("Matarreyes", 205, 150, 0)
eSylas=Habilidades("Fuga", 220, 0, 0)
rSylas=Habilidades("Usurpacion", 0, 0, 0)

qEkko=Habilidades("Rebobinador de tiempo", 260, 0, 0)
wEkko=Habilidades("Convergencia paralela", 0, 0, 160)
eEkko=Habilidades("Salto de fase", 140, 0, 0)
rEkko=Habilidades("Cronorruptura", 450, 200, 0)


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


Campeones=[Kayn, Sylas, Ekko]

print("~---------------------~")
print("| "+ Kayn.getNombre() +" | "+ Sylas.getNombre() +" | "+ Ekko.getNombre() +" |")
print("~---------------------~")

p1=int(input("Elige un personaje"))
print("Has elegido a "+ Campeones[p1].getNombre())
p2=random.randint(0,2)
print("Vas a pelear contra "+ Campeones[p2].getNombre())

while Campeones[p1].getHp() < 0 or Campeones[p2].getNombre() < 0:
    print("~------------------------~")
    print("|               "+ str(Campeones[p2].getHp()) +"|"+ Campeones[p2].getNombre() +" |")
    print("|                        |")
    print("| "+ Campeones[p1].getNombre() +"|"+ str(Campeones[p1].getHp())+"                |")
    print("~---------------------~")


    turno=random.randint(0)


    if turno==0:
        while sk:
            print("Escoge una  habilidad")
            print(Campeones[p1].getHabilidades()[0].getSkillname() + " /Damage: " + str(
                Campeones[p1].getHabilidades()[0].getDamage()) + " /Curacion: " + str(
                Campeones[p1].getHabilidades()[0].getHealth()) + " /Shield: " + str(
                Campeones[p1].getHabilidades()[0].getShield()))
            print(Campeones[p1].getHabilidades()[1].getSkillname() + " /Damage: " + str(
                Campeones[p1].getHabilidades()[1].getDamage()) + " /Curacion: " + str(
                Campeones[p1].getHabilidades()[1].getHealth()) + " /Shield: " + str(
                Campeones[p1].getHabilidades()[1].getShield()))
            print(Campeones[p1].getHabilidades()[2].getSkillname() + " /Damage: " + str(
                Campeones[p1].getHabilidades()[2].getDamage()) + " /Curacion: " + str(
                Campeones[p1].getHabilidades()[2].getHealth()) + " /Shield: " + str(
                Campeones[p1].getHabilidades()[2].getShield()))
            print(Campeones[p1].getHabilidades()[3].getSkillname() + " /Damage: " + str(
                Campeones[p1].getHabilidades()[3].getDamage()) + " /Curacion: " + str(
                Campeones[p1].getHabilidades()[3].getHealth()) + " /Shield: " + str(
                Campeones[p1].getHabilidades()[3].getShield()))
            x=int(input())




