class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    
    def estudiar (self):
        print(F"El estudiante {self.nombre} está estudiando...")

print("Ingrese el nombre del estudiante: ")
nombre = input()
print("Ingrese la edad del estudiante: ")
edad = input()
print("Ingrese el grado del estudiante: ")
grado = input()

nuevo_estudiante = Estudiante(nombre, edad, grado)

estudiar = input("¿Desea estudiar? (S/N): ").upper()
if estudiar == "S":
    nuevo_estudiante.estudiar()
elif estudiar == "N":
    print("Ok")
else:
    print("Ha ingresado un valor incorrecto")