import random

class Habilidades:

    def __init__(self, skillname, damage, health, shield, stun):
        self.skillname = skillname
        self.damage = damage
        self.health = health
        self.shield = shield
        self.stun = stun

    def  getSkillname(self):
        return self.skillname

    def setSkillname(self, skillname):
        self.skillname = skillname

    def getDamage(self):
        return self.damage

    def setDamage(self, damage):
        self.damage = damage

    def getHealth(self):
        return self.health

    def setHealth(self, health):
        self.health = health

    def getShield(self):
        return self.shield

    def setShield(self, shield):
        self.shield = shield

    def  getStun(self):
        return self.stun

    def setStun(self, stun):
        self.stun = stun

    # Modificadores de habilidad Q
    def qSkill(self):
        q=random.randint(0,1)
        if champp1=="Kayn":
            if q == 0:
                self.setDamage(self.getDamage()*2)

        elif champp1=="Sylas":
            q = random.randint(0, 1)
            if q==0:
                self.setDamage(self.getDamage()*1.25)

        elif champp1=="Ekko":
            q = random.randint(0, 1)
            if q==0:
                self.setDamage(self.getDamage()*1.5)

    #Modificadores de habilidad W
    def wSkill(self):
        if champp1=="Kayn":
            self.setDamage(self.getDamage())

        elif champp1=="Sylas":
            if champp1.getHp() < 850:
                self.setDamage(self.getDamage()*1.35)
                self.setHealth(self.getHealth()*1.35)

        elif champp1=="Ekko":
            w = random.randint(0, 1)
            if w==0:
                self.setStun(1)








