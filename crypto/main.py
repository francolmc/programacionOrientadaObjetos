from Crypto.Hash import SHA256

# TODO: crear funcion que encripte la contraseña
def encrypt_pwd(pwd):
    h = SHA256.new()

    h.update(pwd.encode())

    return h.hexdigest()

# TODO: funcion que valide al usuario
def find_user_by_email(email: str):
    # TODO: este ejemplo podria ir a buscar el usuario a la base de datos
    if (email == "pedro@sucorreo.cl"):
        return "f71165b0a6a81299fa71fbdcd27c891df12cb9832c3a5d2a0343466e967cd830";
    else:
        return None

# TODO: Programa principal
user = input("Ingrese usuario (email): ")
password = input("Ingrese la contraseña: ")

hash_password = find_user_by_email(user)

if hash_password == None:
    print("Error: El usuario no existe.")
else:
    if hash_password != encrypt_pwd(password):
        print("Error: los datos no son validos.")
    else:
        print("Acceso aprobado.")