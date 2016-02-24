# Definición

# Abstracción
# Encapsulamiento
# Herencia
# Polimorfismo

class Animal:
    # Atributos (cosas que tiene o que es)
    patas  = 4
    color  = "Verde"
    sonido = ""
    altura = 1.0
    gusta_de = "contradecir"

    # Cosas que hace
    def correr(self):
        print("Estoy corriendo con\
        mis {} patas".format(self.patas))

    def comer(self):
        print("ñam ñam ñam")

    def contradecir(self):
        print("¡Qué no! ¡Qué no!")

class Mamiferos():
    pass

class Gato(Animal):
    sonido = "Miau"

    def say_my_name(self, nombre):
        print("Miau {}".format(nombre))

class Elefante(Animal):
    pass


def hazlo_correr(animal):
    animal.correr()

# Concreción o Instaciamineto
# animal_desconocido = Animal()

# print(animal_desconocido.sonido)
# animal_desconocido.patas = 100
# print(animal_desconocido.patas)

# animal_desconocido.correr()

# animal_2 = Animal()
# print(animal_2.patas)
# animal_2.correr()


pelusa = Gato()      # pelusa es Gato, Gato ""(es un)"" Animal
pelusa.contradecir()
pelusa.say_my_name("Lalo")
print(pelusa.sonido)


dumbo = Elefante()




