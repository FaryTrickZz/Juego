import random

class Personaje:

    def __init__(self, nombre, hp):
        self.nombre = nombre
        self.hp = hp
        self.habilidades=[]

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getHp(self):
        return self.hp

    def setHp(self, hp):
        self.hp = hp

    def getHabilidades(self):
        return self.habilidades

    def setHabilidades(self, habilidad):
        self.habilidades.append(habilidad)

    def getDamage(self, damage):
        self.setHp(self.getHp()-damage)

    def getShield(self, shield):
        self.setHp(self.getHp()+shield)

    def getHealth(self, health):
        self.setHp(self.getHp()+health)

    def elegirHabilidad(self, c):

        if c == 1:
            print("Es el turno de: " + self.getNombre())
            skill = random.randint(1, 4)

            if skill == 1:
                print("El jugador dos ha elegido: " + self.getHabilidades()[0].getSkillname())
                print("Te ha causado: " + str(self.getHabilidades()[0].getDamage()))
                print("Se ha curado: " + str(self.getHabilidades()[0].getHealth()))
                print("Cantidad de escudo obtenida: " + str(self.getHabilidades()[0].getShield()))

            if skill == 2:
                print("El jugador dos ha elegido: " + self.getHabilidades()[1].getSkillname())
                print("Te ha causado: " + str(self.getHabilidades()[1].getDamage()))
                print("Se ha curado: " + str(self.getHabilidades()[1].getHealth()))
                print("Cantidad de escudo obtenida: " + str(self.getHabilidades()[1].getShield()))

            if skill == 3:
                print("El jugador dos ha elegido: " + self.getHabilidades()[2].getSkillname())
                print("Te ha causado: " + str(self.getHabilidades()[2].getDamage()))
                print("Se ha curado: " + str(self.getHabilidades()[2].getHealth()))
                print("Cantidad de escudo obtenida: " + str(self.getHabilidades()[2].getShield()))

            if skill == 4:
                print("El jugador dos ha elegido: " + self.getHabilidades()[3].getSkillname())
                print("Te ha causado: " + str(self.getHabilidades()[3].getDamage()))
                print("Se ha curado: " + str(self.getHabilidades()[3].getHealth()))
                print("Cantidad de escudo obtenida: " + str(self.getHabilidades()[3].getShield()))

        else:
            print("Escoge una habilidad")
            print(self.getHabilidades()[0].getSkillname() + " /Damage: " + str(
                self.getHabilidades()[0].getDamage()) + " /Curacion: " + str(
                self.getHabilidades()[0].getHealth()) + " / Shield: " + str(
                self.getHabilidades()[0].getShield()))

            print(self.getHabilidades()[1].getSkillname() + " /Damage: " + str(
                self.getHabilidades()[1].getDamage()) + " /Curacion: " + str(
                self.getHabilidades()[1].getHealth()) + " /Shield: " + str(
                self.getHabilidades()[1].getShield()))

            print(self.getHabilidades()[2].getSkillname() + " /Damage: " + str(
                self.getHabilidades()[2].getDamage()) + " /Curacion: " + str(
                self.getHabilidades()[2].getHealth()) + " /Shield: " + str(
                self.getHabilidades()[2].getShield()))

            print(self.getHabilidades()[3].getSkillname() + " /Damage: " + str(
                self.getHabilidades()[3].getDamage()) + " /Curacion: " + str(
                self.getHabilidades()[3].getHealth()) + " /Shield: " + str(
                self.getHabilidades()[3].getShield()))

            skill = int(input())

            if skill == 1:
                print("Has elegido: " + self.getHabilidades()[0].getSkillname())
                print("Has causado: " + str(self.getHabilidades()[0].getDamage()))
                print("Te has curado: " + str(self.getHabilidades()[0].getHealth()))
                print("Cantidad de escudo obtenida: " + str(self.getHabilidades()[0].getShield()))

            if skill == 2:
                print("Has elegido: " + self.getHabilidades()[1].getSkillname())
                print("Has causado: " + str(self.getHabilidades()[1].getDamage()))
                print("Te has curado: " + str(self.getHabilidades()[1].getHealth()))
                print("Cantidad de escudo obtenida: " + str(self.getHabilidades()[1].getShield()))

            if skill == 3:
                print("Has elegido: " + self.getHabilidades()[2].getSkillname())
                print("Has causado: " + str(self.getHabilidades()[2].getDamage()))
                print("Te has curado: " + str(self.getHabilidades()[2].getHealth()))
                print("Cantidad de escudo obtenida: " + str(self.getHabilidades()[2].getShield()))

            if skill == 4:
                print("Has elegido: " + self.getHabilidades()[3].getSkillname())
                print("Has causado: " + str(self.getHabilidades()[3].getDamage()))
                print("Te has curado: " + str(self.getHabilidades()[3].getHealth()))
                print("Cantidad de escudo obtenida: " + str(self.getHabilidades()[3].getShield()))

    def restarVida(self, damage):
        self.setHp(self.getHp()-damage)











