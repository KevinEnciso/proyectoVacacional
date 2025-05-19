class Celular:
    def __init__(self, marca, modelo, camara_frontal, camara_trasera):
        self.marca = marca
        self.modelo = modelo
        self.camara_frontal = camara_frontal
        self.camara_trasera = camara_trasera
        self.tipo = "Celular"


    def llamar(self, celular_destino):
        if isinstance(celular_destino, Celular):
            print(f"Llamando a {celular_destino.marca} {celular_destino.modelo} desde {self.marca} {self.modelo}")
        else:
            raise ValueError("El destino debe ser un objeto de la clase Celular")

redmi_12 = Celular("Xiaomi", "Redmi 12", "8MP", "50MP")  
redmi_note_10 = Celular("Xiaomi", "Redmi Note 10", "6MP", "30MP")

redmi_12.llamar(redmi_note_10)