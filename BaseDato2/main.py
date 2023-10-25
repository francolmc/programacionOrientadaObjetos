import sqlite3

DATA_BASE = "ejemplo.db"

def create_movie():
    title = input("Ingresar el nombre de la pelicula: ")
    year = input("Ingresar el año de la pelicula: ")
    score = input("Ingresar la calificación de la pelicula: ")
    connection = sqlite3.connect(DATA_BASE)
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Movies (title, year, score) VALUES ('{title}', '{year}', {score})")
    print("La pelicula fue registrada.")
    connection.commit()
    connection.close()

def find_movie_by_id(id: int):
    connection = sqlite3.connect(DATA_BASE)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Movies WHERE id = {id}")
    return cursor.fetchone()

def edit_movie():
    movie_id = int(input("Ingrese el identificador de la pelicula: "))
    record = find_movie_by_id(movie_id)
    if record == None:
        print("La pelicula que desea editar no existe.")
    else:
        # TODO: Solicitar los nuevos valores para la pelicula mostrando los valores actuales
        titulo = input("Ingresaar titulo pelicula (Pelicula 1): ")
        # TODO: validar que valores quiere modificar el usuario
        # modificar lo singresados por el usuario y mantener los que no ingreso.
        # TODO: Modificar la pelicula
        # TODO: informar al usuario de la pelicula modificada

def delete_movie():
    movie_id = int(input("Ingrese el identificador de la pelicula: "))
    record = find_movie_by_id(movie_id)
    if record == None:
        print("La pelicula que desea eliminar no existe.")
    else:
        pass

def show_movies():
    pass

def create_table():
    # Crear objeto conexion
    connection = sqlite3.connect(DATA_BASE)
    # Crear objeto cursor para realizar operaciones
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE Movies (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT,
                   year INTEGER,
                   score REAL
        )
    """)
    # Guardar los cambios del insert en base de dato
    connection.commit()
    # Cerrar conexion
    connection.close()

option = 0
while option != 6:
    print("1.- Buscar peliculas")
    print("2.- Agregar pelicula")
    print("3.- Editar pelicula")
    print("4.- Eliminar pelicula")
    print("5.- Crear tabla movies")
    print("6.- Salir")
    option = int(input("Ingresar su opcion: "))

    if option == 1:
        show_movies()
    elif option == 2:
        create_movie()
    elif option == 3:
        edit_movie()
    elif option == 4:
        delete_movie()
    elif option == 5:
        create_table()