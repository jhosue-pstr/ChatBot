import mysql.connector

def obtener_conexion():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="infotel_db",
            port=3306
        )
    except mysql.connector.Error as e:
        print(f"❌ Error en la conexión a la base de datos: {str(e)}")
        return None

def agregar_imagen(id_catalogo, imagen_url):
    conn = obtener_conexion()
    if not conn:
        return {"error": "No se pudo conectar a la base de datos"}
    
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO catalogo_imagenes (id_catalogo, imagen_url) VALUES (%s, %s)"
        cursor.execute(sql, (id_catalogo, imagen_url))
        conn.commit()
        return {"mensaje": "Imagen agregada correctamente"}
    except mysql.connector.Error as e:
        return {"error": f"Error al agregar imagen: {str(e)}"}
    finally:
        cursor.close()
        conn.close()


def obtener_imagenes(id_catalogo):
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT id_imagen, imagen_url FROM catalogo_imagenes WHERE id_catalogo = %s"
    cursor.execute(query, (id_catalogo,))
    resultado = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"imagenes": [{"id": img["id_imagen"], "url": img["imagen_url"]} for img in resultado] if resultado else {"imagenes": []}}

def eliminar_imagen(id_imagen):
    conn = obtener_conexion()
    if not conn:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM catalogo_imagenes WHERE id_imagen = %s", (id_imagen,))
        conn.commit()
        return {"mensaje": "Imagen eliminada correctamente"}
    except mysql.connector.Error as e:
        return {"error": f"Error al eliminar imagen: {str(e)}"}
    finally:
        cursor.close()
        conn.close()


