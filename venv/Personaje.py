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
