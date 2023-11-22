from Crypto.Hash import SHA256
import sqlite3

DATA_BASE = "users.db"

def create_user():
    username = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")
    # Encriptación de la contraseña con SHA256
    hashed_password = SHA256.new(password.encode()).hexdigest()
    connection = sqlite3.connect(DATA_BASE)
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Users (username, password) VALUES ('{username}', '{hashed_password}')")
    print("Usuario registrado exitosamente.")
    connection.commit()
    connection.close()

def authenticate_user():
    username = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")
    # Encriptación de la contraseña con SHA256
    hashed_password = SHA256.new(password.encode()).hexdigest()
    connection = sqlite3.connect(DATA_BASE)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Users WHERE username='{username}' AND password='{hashed_password}'")
    user = cursor.fetchone()
    connection.close()
    if user:
        print("Inicio de sesión exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

def create_table():
    connection = sqlite3.connect(DATA_BASE)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        ) """)
    connection.commit()
    connection.close()

def check_database():
    try:
        connection = sqlite3.connect(DATA_BASE)
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM Users LIMIT 1")
        connection.close()
    except sqlite3.OperationalError as err:
        print("ERROR: La tabla Usuarios no existe, seleccione la opcion 3 para crear la tabla.")

check_database()

option = 0
while option != 4:
    print("1.- Registrar usuario")
    print("2.- Iniciar sesión")
    print("3.- Crear tabla usuarios")
    print("4.- Salir")
    option = int(input("Ingrese su opción: "))
    if option == 1:
        create_user()
    elif option == 2:
        authenticate_user()
    elif option == 3:
        create_table()
    elif option == 4:
        break