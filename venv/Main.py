from Personaje import Personaje
from Habilidades import Habilidades
from ListaPersonajes import ListaPersonajes
import random
from os import system, name

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

Lista1=ListaPersonajes("Lista Campeones")
Lista1.setCampeones(Kayn)
Lista1.setCampeones(Sylas)
Lista1.setCampeones(Ekko)

print("~---------------------~")
print("| "+ Lista1.getCampeones()[0].getNombre() +" | "+Lista1.getCampeones()[1].getNombre() +" | "+Lista1.getCampeones()[2].getNombre() +" | ")
print("~---------------------~")

p1=int(input("Elige un personaje"))
p2=random.randint(0,2)
while p2 == p1:
    p2 = random.randint(0, 2)

p1=Lista1.getCampeones()[p1]
p2=Lista1.getCampeones()[p2]
print("Has elegido a "+ p1.getNombre())
print("Vas a pelear contra "+ p2.getNombre())


while  p1.getHp() > 0 and p2.getHp() > 0:
    print("~------------------------~")
    print("|               "+ str(p2.getHp()) +"|"+ p2.getNombre() +" |")
    print("|                        |")
    print("| "+  p1.getNombre() +"|"+ str( p1.getHp())+"                |")
    print("~---------------------~")


    x=0
    for h in p1.getHabilidades():
        print (str(x)+" "+h.getSkillname()+ " /Damage: "+str(h.getDamage())+" /Health: "+str(h.getHealth())+" /Shield: "+str(h.getShield()))
        x=x+1
    habilidadp1 = int(input("Elige una habilidad"))
    p2.restarVida(p1.getHabilidades()[habilidadp1].getDamage())

    x=0




