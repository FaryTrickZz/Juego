class ListaPersonajes:

    def __init__(self, nombre):
        self.nombre = nombre
        self.Campeones = []

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getCampeones(self):
        return self.Campeones

    def setCampeones(self, Campeones):
        self.Campeones.append(Campeones)
