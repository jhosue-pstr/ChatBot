import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="infotel_db",
        port=3306
    )


def crear_comprobante_pago(id_exportacion, id_importacion, numero, fecha_emision, subtotal, descuento_total, impuesto, total, tipo_documento, archivo_url):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        INSERT INTO comprobante_pago 
        (id_exportacion, id_importacion, numero, fecha_emision, subtotal, descuento_total, impuesto, total, tipo_documento, archivo_url)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (id_exportacion, id_importacion, numero, fecha_emision, subtotal, descuento_total, impuesto, total, tipo_documento, archivo_url))
    conexion.commit()
    cursor.close()
    conexion.close()

def listar_comprobantes_pago():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM comprobante_pago")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def obtener_comprobante_pago(id_comprobante):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM comprobante_pago WHERE id_comprobante = %s", (id_comprobante,))
    comprobante = cursor.fetchone()
    cursor.close()
    conexion.close()
    return comprobante

def actualizar_comprobante_pago(id_comprobante, id_exportacion, id_importacion, numero, fecha_emision, subtotal, descuento_total, impuesto, total, tipo_documento, archivo_url):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        UPDATE comprobante_pago
        SET id_exportacion = %s, id_importacion = %s, numero = %s, fecha_emision = %s,
            subtotal = %s, descuento_total = %s, impuesto = %s, total = %s,
            tipo_documento = %s, archivo_url = %s
        WHERE id_comprobante = %s
    """
    cursor.execute(sql, (id_exportacion, id_importacion, numero, fecha_emision, subtotal, descuento_total, impuesto, total, tipo_documento, archivo_url, id_comprobante))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_comprobante_pago(id_comprobante):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM comprobante_pago WHERE id_comprobante = %s", (id_comprobante,))
    conexion.commit()
    cursor.close()
    conexion.close()
