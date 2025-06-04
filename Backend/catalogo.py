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
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT c.*, 
        COALESCE(GROUP_CONCAT(ci.imagen_url SEPARATOR ','), '') AS imagenes
        FROM catalogo c
        LEFT JOIN catalogo_imagenes ci ON c.id_catalogo = ci.id_catalogo
        GROUP BY c.id_catalogo
    """

    cursor.execute(query)
    productos = cursor.fetchall()

    # ✅ Convertir imágenes concatenadas en un array
    for producto in productos:
        producto['imagenes'] = producto['imagenes'].split(',') if producto['imagenes'] else []

    cursor.close()
    conn.close()
    return productos


def obtener_catalogo(id_catalogo):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    query = """
        SELECT c.*, 
        COALESCE(GROUP_CONCAT(ci.imagen_url SEPARATOR ','), NULL) AS imagenes
        FROM catalogo c
        LEFT JOIN catalogo_imagenes ci ON c.id_catalogo = ci.id_catalogo
        WHERE c.id_catalogo = %s
        GROUP BY c.id_catalogo
    """

    cursor.execute(query, (id_catalogo,))
    catalogo = cursor.fetchone()

    if catalogo:
        # ✅ Corregir el problema de `imagenes`
        catalogo['imagenes'] = catalogo['imagenes'].split(',') if catalogo['imagenes'] and catalogo['imagenes'] != "None" else []

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


def buscar_por_nombre(nombre_filtro):
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM catalogo WHERE nombre LIKE %s"
    cursor.execute(query, (f"%{nombre_filtro}%",))
    productos = cursor.fetchall()

    cursor.close()
    conn.close()

    return productos