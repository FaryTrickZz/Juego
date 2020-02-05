# -*- coding: UTF-8 -*-

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

    def getStun(self):
        return self.stun

    def setStun(self, stun):
        self.stun = stun

    # Modificadores de habilidad Q
    def qSkill(self, champ):

        if champ=="Kayn":
            q = random.randint(0, 1)
            if q == 0:
                self.setDamage(self.getDamage()*2)
            else:
                self.setDamage(self.getDamage())

            print("  ××××××××××××××××××××××××××××××××××××××  ")
            print("   Kayn: "+ self.getSkillname())
            print("  ××××××××××××××××××××××××××××××××××××××  ")

        elif champ=="Sylas":
            q = random.randint(0, 1)
            if q==0:
                self.setDamage(self.getDamage()*1.25)
            else:
                self.setDamage(self.getDamage())

            print("  ××××××××××××××××××××××××××××××××××××××  ")
            print("   Sylas: " + self.getSkillname())
            print("  ××××××××××××××××××××××××××××××××××××××  ")

        elif champ=="Ekko":
            q = random.randint(0, 1)
            if q==0:
                self.setDamage(self.getDamage()*1.5)
            else:
                self.setDamage(self.getDamage())

            print("  ××××××××××××××××××××××××××××××××××××××  ")
            print("   Ekko: " + self.getSkillname())
            print("  ××××××××××××××××××××××××××××××××××××××  ")

    #Modificadores de habilidad W
    def wSkill(self, champ):
        if champ=="Kayn":
            self.setDamage(self.getDamage())

            print("  ××××××××××××××××××××××××××××××××××××××  ")
            print("   Kayn: " + self.getSkillname())
            print("  ××××××××××××××××××××××××××××××××××××××  ")

        elif champ=="Sylas":
            w = random.randint(0, 5)
            if w == 5:
                self.setDamage(self.getDamage()*1.35)
                self.setHealth(self.getHealth()*1.35)
            else:
                self.setDamage(self.getDamage())
                self.setHealth(self.getHealth())

            print("  ××××××××××××××××××××××××××××××××××××××  ")
            print("   Sylas: " + self.getSkillname())
            print("  ××××××××××××××××××××××××××××××××××××××  ")

        elif champ=="Ekko":
            w = random.randint(0,1)
            if w==0:
                self.setStun(self.getStun()+1)
            else:
                self.setStun(0)

            print("  ××××××××××××××××××××××××××××××××××××××  ")
            print("   Ekko: " + self.getSkillname())
            print("  ××××××××××××××××××××××××××××××××××××××  ")

    # Modificadores de habilidad E
    def eSkill(self, champ):
        if champ=="Kayn":
            self.setHealth(self.getHealth())

            print("  ××××××××××××××××××××××××××××××××××××××  ")
            print("   Kayn: " + self.getSkillname())
            print("  ××××××××××××××××××××××××××××××××××××××  ")

        elif champ=="Sylas":
            e = random.randint(0,1)
            if e == 1:
                self.setDamage(self.getDamage())
                self.setStun(self.getStun()+1)
            else:
                self.setDamage(self.getDamage())

            print("  ××××××××××××××××××××××××××××××××××××××  ")
            print("   Sylas: " + self.getSkillname())
            print("  ××××××××××××××××××××××××××××××××××××××  ")

        elif champ=="Ekko":
                self.setDamage(self.getDamage())

        print("  ××××××××××××××××××××××××××××××××××××××  ")
        print("   Ekko: " + self.getSkillname())
        print("  ××××××××××××××××××××××××××××××××××××××  ")

    def rSkill(self, champ, champ2):
        if champ=="Kayn":
            self.setStun(self.getStun()+1)
            print("Kayn se ha hecho invulnerable")

            print("  ××××××××××××××××××××××××××××××××××××××  ")
            print("   Sylas: " + self.getSkillname())
            print("  ××××××××××××××××××××××××××××××××××××××  ")

        elif champ=="Sylas":
            self.setStun(champ2.getHabilidades()[3].getStun())
            self.setDamage(champ2.getHabilidades()[3].getDamage())
            self.setHealth(champ2.getHabilidades()[3].getHealth())
            self.setShield(champ2.getHabilidades()[3].getShield())

            print("  ××××××××××××××××××××××××××××××××××××××  ")
            print("   Sylas: " + self.getSkillname())
            print("  ××××××××××××××××××××××××××××××××××××××  ")


        elif champ=="Ekko":
            self.setDamage(self.getDamage())

            print("  ××××××××××××××××××××××××××××××××××××××  ")
            print("   Ekko: " + self.getSkillname())
            print("  ××××××××××××××××××××××××××××××××××××××  ")






