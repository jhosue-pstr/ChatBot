import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="infotel_db",
        port=3306
    )


def crear_almacen(id_producto, cantidad_disponible, cantidad_minima, ubicacion, fecha_entrada, estado):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        INSERT INTO almacen (id_producto, cantidad_disponible, cantidad_minima, ubicacion, fecha_entrada, estado)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (id_producto, cantidad_disponible, cantidad_minima, ubicacion, fecha_entrada, estado))
    conexion.commit()
    cursor.close()
    conexion.close()

def listar_almacen():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM almacen")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def obtener_almacen(id_almacen):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM almacen WHERE id_almacen = %s", (id_almacen,))
    almacen = cursor.fetchone()
    cursor.close()
    conexion.close()
    return almacen

def actualizar_almacen(id_almacen, id_producto, cantidad_disponible, cantidad_minima, ubicacion, fecha_entrada, estado):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        UPDATE almacen
        SET id_producto = %s, cantidad_disponible = %s, cantidad_minima = %s, ubicacion = %s, fecha_entrada = %s, estado = %s
        WHERE id_almacen = %s
    """
    cursor.execute(sql, (id_producto, cantidad_disponible, cantidad_minima, ubicacion, fecha_entrada, estado, id_almacen))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_almacen(id_almacen):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM almacen WHERE id_almacen = %s", (id_almacen,))
    conexion.commit()
    cursor.close()
    conexion.close()
