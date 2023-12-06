class Personaje:
    def __init__(self, nombre, especie, estado):
        self.nombre = nombre
        self.especie = especie
        self.estado = estado

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}\nEspecie: {self.especie}\nEstado: {self.estado}")


import requests
import json

def obtener_personaje_api_por_id(id):
    url = f"https://rickandmortyapi.com/api/character/{id}"
    response = requests.get(url)
    json_data = response.text
    personaje_json = json.loads(json_data)
    return personaje_json


import sqlite3

class GestorBaseDatos:
    def __init__(self):
        self.conexion = sqlite3.connect("rick_and_morty.db")
        self.cursor = self.conexion.cursor()

    def crear_tabla_personajes(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Personajes (
                ID INTEGER PRIMARY KEY,
                nombre TEXT,
                especie TEXT,
                estado TEXT
            )
        ''')
        self.conexion.commit()

    def insertar_personaje(self, personaje: Personaje):
        self.cursor.execute("INSERT INTO Personajes (nombre, especie, estado) VALUES (?, ?, ?)",
                            (personaje.nombre, personaje.especie, personaje.estado))
        self.conexion.commit()

    def obtener_personarjes(self):
        self.cursor.execute("SELECT nombre, especie, estado FROM Personajes")
        result = self.cursor.fetchall()
        personajes = list()
        for item in result:
            personajes.append(Personaje(item[0], item[1], item[2]))
        return personajes

def menu_aplicacion():
    gestor_bd = GestorBaseDatos()
    gestor_bd.crear_tabla_personajes()

    while True:
        print("\n==== Menú de Aplicación ====")
        print("1. Mostrar información de personajes")
        print("2. Insertar un nuevo personaje")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            personajes = gestor_bd.obtener_personarjes()
            for personaje in personajes:
                personaje.mostrar_info()
 
        elif opcion == "2":
            id_personaje = input("Ingrese el ID del personaje: ")
            personaje_ra = obtener_personaje_api_por_id(id_personaje)
            nuevo_personaje = Personaje(personaje_ra["name"], personaje_ra["status"], personaje_ra["species"])
            gestor_bd.insertar_personaje(nuevo_personaje)
            print("Personaje insertado con éxito.")

        elif opcion == "3":
            # Salir de la aplicación
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")


menu_aplicacion()