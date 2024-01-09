import sqlite3
from Crypto.Hash import SHA256

class Usuario:
    def __init__(self, nombre, email, password, rol='usuario'):
        self.nombre = nombre
        self.email = email
        self.password = password
        self.rol = rol

    def encriptar_password(self):
        # Utilizar SHA256 para el hashing seguro de contraseñas
        hashed_password = SHA256.new(self.password.encode()).hexdigest()
        return hashed_password

    def validar_password(self, password):
        # Validar la contraseña encriptada con SHA256
        hashed_password = SHA256.new(password.encode()).hexdigest()
        hashed_password2 = SHA256.new(password.encode()).hexdigest()
        return self.password == SHA256.new(password.encode()).hexdigest()

class GestorBaseDatos:
    def __init__(self, nombre_bd='usuarios.db'):
        self.conexion = sqlite3.connect(nombre_bd)
        self.cursor = self.conexion.cursor()

    def crear_tabla_usuarios(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                email TEXT UNIQUE,
                password TEXT,
                rol TEXT
            )
        ''')
        self.conexion.commit()

    def crear_usuario_inicial(self):
        # Crear un usuario inicial (admin) al inicializar la aplicación
        admin = Usuario('Admin', 'admin@example.com', 'admin_password', 'admin')
        self.insertar_usuario(admin)
        self.conexion.commit()

    def insertar_usuario(self, usuario:Usuario):
        self.cursor.execute('''
            INSERT INTO usuarios (nombre, email, password, rol) VALUES (?, ?, ?, ?)
        ''', (usuario.nombre, usuario.email, usuario.encriptar_password(), usuario.rol))
        self.conexion.commit()

    def buscar_usuario_por_email(self, email):
        self.cursor.execute("SELECT * FROM usuarios WHERE email=?", (email,))
        resultado = self.cursor.fetchone()
        if resultado:
            return Usuario(resultado[1], resultado[2], resultado[3], resultado[4])
        return None
    
    def cerrar_conexion(self):
        self.conexion.close()

def acceso(email:str, password:str) -> bool:
    gestor_bd = GestorBaseDatos()
    usuario = gestor_bd.buscar_usuario_por_email(email)
    gestor_bd.cerrar_conexion()
    if (usuario == None):
        return False
    return usuario.validar_password(password)

def inicializar_app():
    gestor_bd = GestorBaseDatos()
    gestor_bd.crear_tabla_usuarios()
    if (gestor_bd.buscar_usuario_por_email("admin@example.com") == None):
        gestor_bd.crear_usuario_inicial()
    gestor_bd.cerrar_conexion()

def menu_usuario():
    gestor_bd = GestorBaseDatos()
    while True:
        print("\n==== Menú de Usuario ====")
        print("1. Buscar Usuario por Email")
        print("2. Registrar usuario")
        print("3. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Buscar usuario por email
            email = input("Ingrese el email del usuario a buscar: ")
            usuario = gestor_bd.buscar_usuario_por_email(email)
            if usuario:
                print(f"Usuario encontrado: {usuario.nombre}, {usuario.email}, {usuario.rol}")
            else:
                print("Usuario no encontrado.")
        elif opcion == "2":
            # Registro de usuario
            nombre = input("Ingrese su nombre: ")
            email = input("Ingrese su email: ")
            password = input("Ingrese su contraseña: ")
            nuevo_usuario = Usuario(nombre, email, password)
            gestor_bd.insertar_usuario(nuevo_usuario)
            print("¡Usuario registrado con éxito!")
        elif opcion == "3":
            # Cerrar sesión y volver al menú principal
            print("Cerrando sesión. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
    gestor_bd.cerrar_conexion()


# Inicio de la aplicacion
inicializar_app()
email = input("Ingresar email: ")
password = input("Ingresar contrasena ")
if (acceso(email, password)):
    # Ejecutar la aplicación
    menu_usuario()
else:
    print("Ud. no tiene acceso a la plataforma.")
