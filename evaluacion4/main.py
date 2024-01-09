import sqlite3
import requests

class Entidad:
    def __init__(self, id):
        self.id = id

    def mostrar_info(self):
        print(f"ID: {self.id}")

class APIClient:
    def obtener_publicacion(self, codigo_publicacion):
        url = f'https://jsonplaceholder.typicode.com/posts/{codigo_publicacion}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None

class Publicacion(Entidad):
    def __init__(self, id, usuario_id, titulo, contenido):
        super().__init__(id)
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.contenido = contenido

    def __str__(self) -> str:
        return f"{self.id}\t{self.usuario_id}\t{self.titulo}\t{self.contenido}"

class BaseDatos:
    def __init__(self, nombre_bd='publicaciones.db'):
        self.conexion = sqlite3.connect(nombre_bd)
        self.cursor = self.conexion.cursor()

    def conectar_bd(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Publicaciones (
                ID INTEGER PRIMARY KEY, 
                ID_Autor INTEGER, 
                Titulo TEXT, 
                Contenido TEXT
            )
        ''')
        self.conexion.commit()

    def insertar_publicacion(self, publicacion):
        self.cursor.execute('''
            INSERT INTO Publicaciones (ID, ID_Autor, Titulo, Contenido) VALUES (?, ?, ?, ?)
        ''', (publicacion.id, publicacion.usuario_id, publicacion.titulo, publicacion.contenido))
        self.conexion.commit()

    def consultar_publicaciones(self):
        self.cursor.execute("SELECT * FROM Publicaciones")
        return self.cursor.fetchall()

    def eliminar_publicacion(self, publicacion_id):
        self.cursor.execute("DELETE FROM Publicaciones WHERE ID=?", (publicacion_id,))
        self.conexion.commit()

    def buscar_publicacion_por_id(self, publicacion_id):
        self.cursor.execute("SELECT * FROM Publicaciones WHERE ID=?", (publicacion_id))
        return self.cursor.fetchone()

class Aplicacion:
    def __init__(self, api_client:APIClient, base_datos:BaseDatos):
        self.api_client = api_client
        self.base_datos = base_datos

    def ejecutar(self):
        while True:
            print("\nMenú:")
            print("1. Ingresar Publicación desde API a Base de Datos")
            print("2. Mostrar Todas las Publicaciones en Base de Datos")
            print("3. Eliminar una Publicación de la Base de Datos")
            print("4. Salir")

            opcion = int(input("Ingrese su opción: "))

            if opcion == 1:
                self.ingresar_publicacion_desde_api()
            elif opcion == 2:
                self.mostrar_todas_las_publicaciones()
            elif opcion == 3:
                self.eliminar_publicacion_de_bd()
            elif opcion == 4:
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")

    def ingresar_publicacion_desde_api(self):
        codigo_publicacion = int(input("Ingrese el código de la publicación: "))
        if self.base_datos.buscar_publicacion_por_id(codigo_publicacion) == None:
            publicacion_data = self.api_client.obtener_publicacion(codigo_publicacion)
            if publicacion_data:
                publicacion = Publicacion(publicacion_data['id'], publicacion_data['userId'], publicacion_data['title'], publicacion_data['body'])
                self.base_datos.insertar_publicacion(publicacion)
                print("Publicación ingresada con éxito.")
            else:
                print("No se pudo obtener la publicación desde la API.")
        else:
            print("La publicacion ya se encuentra registrada.")

    def mostrar_todas_las_publicaciones(self):
        publicaciones = self.base_datos.consultar_publicaciones()
        if publicaciones:
            for publicacion in publicaciones:
                p = Publicacion(publicacion[0], publicacion[1], publicacion[2], publicacion[3])
                print(p)
        else:
            print("No hay publicaciones en la base de datos.")

    def eliminar_publicacion_de_bd(self):
        publicacion_id = int(input("Ingrese el ID de la publicación a eliminar: "))
        if self.base_datos.buscar_publicacion_por_id(publicacion_id) != None:
            self.base_datos.eliminar_publicacion(publicacion_id)
            print("Publicación eliminada con éxito.")
        else:
            print("La publicacion solicitada para eliminar no existe.")

api_client = APIClient()
base_datos = BaseDatos()
base_datos.conectar_bd()

aplicacion = Aplicacion(api_client, base_datos)
aplicacion.ejecutar()