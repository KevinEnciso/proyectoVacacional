class Persona:
    def __init__(self, nombre:str, edad:int):
        self.nombre = nombre
        self.edad = edad
    

    def soy (self):
        print(f"Mi nombre es {self.nombre} y tengo {self.edad}")


class Estudiante (Persona):
    def __init__(self, nombre:str, edad:int, grado:int):
        super().__init__(nombre, edad)
        self.grado = grado

    def mi_grado (self):
        print(f"Mi nombre es {self.nombre}, tengo {self.edad} y soy de {self.grado}° grado")


estudiante_1 = Estudiante("Juan", 16, 11)
persona_1 = Persona("Marcos", 16)

estudiante_1.mi_grado()
persona_1.soy()
estudiante_1.soy()