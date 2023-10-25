
# Crear objeto conexion
connection = sqlite3.connect("ejemplo.db")
# Cerrar conexion
connection.close()











# Crear objeto cursor para realizar operaciones
cursor = conexion.cursor()
# Crear tabla en la base de datos
# cursor.execute("CREATE TABLE movie(title, year, score)")
# Ejecutar SQL Insert
# cursor.execute("""
#     INSERT INTO movie VALUES
#         ('Monty Python and the Holy Grail', 1975, 8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)
# Guardar los cambios del insert en base de dato
# conexion.commit()

consulta = cursor.execute("SELECT * FROM Movie")
registros = consulta.fetchall()

for record in registros:
    print(f"Title: {record[0]}, Year: {record[1]}, Score: {record[2]}")

# Cerrar conexion
conexion.close()