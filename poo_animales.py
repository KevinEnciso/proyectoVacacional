class Animal:
    def __init__(self, nombre, altura, peso):
        self.nombre = nombre
        self.altura = altura
        self.peso = peso


class Planta:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color


class Carnivoro(Animal):
    def __init__(self, nombre, altura, peso, base_alimenticia):
        super().__init__(nombre, altura, peso)
        if isinstance(base_alimenticia, Animal):
            self.base_alimenticia = base_alimenticia
        else:
            print("Los carnívoros solo comen animales")

class Herbivoro(Animal):
    def __init__(self, nombre, altura, peso, base_alimenticia):
        super().__init__(nombre, altura, peso)
        if isinstance(base_alimenticia, Planta):
            self.base_alimenticia = base_alimenticia
        else:
            print("Los herbívoros solo comen plantas")

class Omnivoro(Carnivoro, Herbivoro):
    pass