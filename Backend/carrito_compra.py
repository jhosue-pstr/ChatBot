import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="infotel_db",
        port=3306
    )

def agregar_item_carrito(id_catalogo, cantidad_producto, precio_unitario):
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = """
            INSERT INTO carrito_compra (id_catalogo, cantidad_producto, precio_unitario)
            VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (id_catalogo, cantidad_producto, precio_unitario))
        conexion.commit()
        cursor.close()
        conexion.close()
        return {"mensaje": "Item agregado al carrito con éxito"}, 201
    except Exception as e:
        return {"error": str(e)}, 400

def listar_carrito():
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        sql = """
            SELECT
                c.id_carrito,
                c.id_catalogo,
                ca.nombre AS nombre_producto,
                ca.precio AS precio_unitario,
                c.cantidad_producto,
                (ca.precio * c.cantidad_producto) AS subtotal
            FROM carrito_compra c
            JOIN catalogo ca ON c.id_catalogo = ca.id_catalogo
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultados
    except Exception as e:
        return {"error": str(e)}, 500

def obtener_item_carrito(id_carrito):
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM carrito_compra WHERE id_carrito = %s", (id_carrito,))
        item = cursor.fetchone()
        cursor.close()
        conexion.close()
        return item if item else {"mensaje": "Item no encontrado"}, 404
    except Exception as e:
        return {"error": str(e)}, 500

def actualizar_item_carrito(id_carrito, id_catalogo, cantidad_producto, precio_unitario):
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = """
            UPDATE carrito_compra
            SET id_catalogo = %s, cantidad_producto = %s, precio_unitario = %s
            WHERE id_carrito = %s
        """
        cursor.execute(sql, (id_catalogo, cantidad_producto, precio_unitario, id_carrito))
        conexion.commit()
        cursor.close()
        conexion.close()
        return {"mensaje": "Item actualizado correctamente"}, 200
    except Exception as e:
        return {"error": str(e)}, 400

def eliminar_item_carrito(id_carrito):
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM carrito_compra WHERE id_carrito = %s", (id_carrito,))
        conexion.commit()
        cursor.close()
        conexion.close()
        return {"mensaje": "Item eliminado correctamente"}, 200
    except Exception as e:
        return {"error": str(e)}, 400
