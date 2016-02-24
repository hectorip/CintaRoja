class Animal:
    patas = 4
    max_vel = 30

    def avanzar(self):
        pass


class Vehiculo:
    llantas = 2
    max_vel = 20

    def avanzar(self):
        pass


class Caballo(Vehiculo, Animal):
    llantas = 0

caballito = Caballo()
print(caballito.max_vel)

