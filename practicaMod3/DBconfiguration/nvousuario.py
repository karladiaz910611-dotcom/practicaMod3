import os
import psycopg2
import getpass
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "credenciales")
DB_USER = os.getenv("DB_USER", "Admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "p4ssw0rdDB")
def conectar_db():
    try:
        return psycopg2.connect(
            host=DB_HOST, port=DB_PORT,
            database=DB_NAME, user=DB_USER, password=DB_PASSWORD
        )
    except Exception as e:
        print("Error de conexión:", e)
        return None

def insertar_usuario(nombre, correo, telefono, fecha_nacimiento):
    conn = conectar_db()
    if not conn:
        return
    try:
        with conn.cursor() as cursor:
            cursor.execute('''
            INSERT INTO usuarios (nombre, correo, telefono, fecha_nacimiento) VALUES (%s, %s, %s, %s)
            ''', (nombre, correo, telefono, fecha_nacimiento))
            conn.commit()

    except Exception as e:
        print(cursor)
        print("Error al conectar con la base de datos:", e)
    finally:
        conn.close()
if __name__ == "__main__":
    print("Agregar un nuevo usuario")
    nombre = input("Ingrese el nombre: ")
    correo = input("Ingrese el correo: ")
    telefono = input("Ingrese el telefono: ")
    fecha_nacimiento = input("Ingrese el fecha_nacimiento: ")
    insertar_usuario(nombre, correo, telefono, fecha_nacimiento)
