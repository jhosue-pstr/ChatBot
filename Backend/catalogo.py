import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="infotel_db",
        port=3306
    )

def crear_catalogo(nombre, descripcion, talla, color, material, precio, stock, id_tipo, id_categoria, imagen_url):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        INSERT INTO catalogo (nombre, descripcion, talla, color, material, precio, stock, id_tipo, id_categoria, imagen_url)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (nombre, descripcion, talla, color, material, precio, stock, id_tipo, id_categoria, imagen_url))
    conexion.commit()
    cursor.close()
    conexion.close()

def listar_catalogo():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM catalogo")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def obtener_catalogo(id_catalogo):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM catalogo WHERE id_catalogo = %s", (id_catalogo,))
    catalogo = cursor.fetchone()
    cursor.close()
    conexion.close()
    return catalogo

def actualizar_catalogo(id_catalogo, nombre, descripcion, talla, color, material, precio, stock, id_tipo, id_categoria, imagen_url):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        UPDATE catalogo
        SET nombre = %s, descripcion = %s, talla = %s, color = %s, material = %s, precio = %s, stock = %s, id_tipo = %s, id_categoria = %s, imagen_url = %s
        WHERE id_catalogo = %s
    """
    cursor.execute(sql, (nombre, descripcion, talla, color, material, precio, stock, id_tipo, id_categoria, imagen_url, id_catalogo))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_catalogo(id_catalogo):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM catalogo WHERE id_catalogo = %s", (id_catalogo,))
    conexion.commit()
    cursor.close()
    conexion.close()
