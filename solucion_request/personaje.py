class Personaje:
    def __init__(self, nombre, especie, estado):
        self.nombre = nombre
        self.especie = especie
        self.estado = estado

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}\nEspecie: {self.especie}\nEstado: {self.estado}")