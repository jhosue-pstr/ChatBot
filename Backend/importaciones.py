import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="infotel_db",
        port=3306
    )


def crear_importacion(id_proveedor, id_compra, descripcion, fecha_ingreso, documento_ingreso, id_comprobante):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        INSERT INTO importaciones (id_proveedor, id_compra, descripcion, fecha_ingreso, documento_ingreso, id_comprobante)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (id_proveedor, id_compra, descripcion, fecha_ingreso, documento_ingreso, id_comprobante))
    conexion.commit()
    cursor.close()
    conexion.close()

def listar_importaciones():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM importaciones")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def obtener_importacion(id_importacion):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM importaciones WHERE id_importacion = %s", (id_importacion,))
    importacion = cursor.fetchone()
    cursor.close()
    conexion.close()
    return importacion

def actualizar_importacion(id_importacion, id_proveedor, id_compra, descripcion, fecha_ingreso, documento_ingreso, id_comprobante):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        UPDATE importaciones
        SET id_proveedor = %s, id_compra = %s, descripcion = %s, fecha_ingreso = %s, documento_ingreso = %s, id_comprobante = %s
        WHERE id_importacion = %s
    """
    cursor.execute(sql, (id_proveedor, id_compra, descripcion, fecha_ingreso, documento_ingreso, id_comprobante, id_importacion))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_importacion(id_importacion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM importaciones WHERE id_importacion = %s", (id_importacion,))
    conexion.commit()
    cursor.close()
    conexion.close()
