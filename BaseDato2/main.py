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
        print("Ingresa los valores a modificar, en caso de no moficiar solo preciona enter.")
        title = input(f"Ingresar titulo pelicula ({record[1]}): ")
        year = input(f"Ingresar año pelicula ({record[2]}): ")
        score = input(f"Ingresar puntaje pelicula ({record[3]}): ")
        # TODO: validar que valores quiere modificar el usuario
        # modificar lo singresados por el usuario y mantener los que no ingreso.
        title_update = record[1]
        if (len(title)>0):
            title_update = title
        year_update = record[2]
        if (len(year)>0):
            year_update = year
        score_update = record[3]
        if (len(score)>0):
            score_update = score
        # TODO: Modificar la pelicula
        connection = sqlite3.connect(DATA_BASE)
        cursor = connection.cursor()
        cursor.execute(f"UPDATE Movies SET title='{title_update}', year='{year_update}', score='{score_update}' WHERE id='{movie_id}'")
        connection.commit()
        connection.close()
        # TODO: informar al usuario de la pelicula modificada
        print("La pelicula fue modificada.")
def delete_movie():
    movie_id = int(input("Ingrese el identificador de la pelicula: "))
    record = find_movie_by_id(movie_id)
    if record == None:
        print("La pelicula que desea eliminar no existe.")
    else:
        connection = sqlite3.connect(DATA_BASE)
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM Movies WHERE id={movie_id}")
        connection.commit()
        connection.close()
        print("La pelicula fue modificada.")

def show_movies():
    title_filter = input("Ingrese el nombre de la pelicula: ")
    connection = sqlite3.connect(DATA_BASE)
    cursor = connection.cursor()
    cursor.execute(f"SELECT id, title, year, score FROM Movies WHERE title LIKE '%{title_filter}%'")
    records = cursor.fetchall()
    for record in records:
        print(f"id: {record[0]} \t title: {record[1]} \t year: {record[2]} \t score: {record[3]}")
    connection.close()

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

def check_database():
    try:
        connection = sqlite3.connect(DATA_BASE)
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM Movies LIMIT 1")
        connection.close()
    except sqlite3.OperationalError as err:
        print("ERROR: La tabla Movies no existe, seleccione la opcion 5 para crear la tabla.")

check_database()
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