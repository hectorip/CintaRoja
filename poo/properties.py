class Persona:

    def __init__(self, estatura, nombre):
        self.nombre = nombre
        self._estatura = estatura

    @property
    def estatura(self):
        return self._estatura

    @estatura.setter
    def estatura(self, estatura):
        if estatura > 2:
            estatura = 2
        self._estatura = estatura


