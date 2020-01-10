class Habilidades:

    def __init__(self, skillname, damage, health, shield):
        self.skillname = skillname
        self.damage = damage
        self.health = health
        self.shield = shield

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

    def sumarHealth(self, health):
        self.health = health

    def getShield(self):
        return self.shield

    def setshield(self, shield):
        self.shield = shield

    def rSylas(self,damage):
        self.setDamage(damage)



