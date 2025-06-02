import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="infotel_db",
        port=3306
    )


def crear_exportacion(id_venta, id_comprobante, pais_destino, descripcion_carga, fecha_envio):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        INSERT INTO exportaciones 
        (id_venta, id_comprobante, pais_destino, descripcion_carga, fecha_envio)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (id_venta, id_comprobante, pais_destino, descripcion_carga, fecha_envio))
    conexion.commit()
    cursor.close()
    conexion.close()

def listar_exportaciones():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM exportaciones")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def obtener_exportacion(id_exportacion):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM exportaciones WHERE id_exportacion = %s", (id_exportacion,))
    exportacion = cursor.fetchone()
    cursor.close()
    conexion.close()
    return exportacion

def actualizar_exportacion(id_exportacion, id_venta, id_comprobante, pais_destino, descripcion_carga, fecha_envio):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        UPDATE exportaciones
        SET id_venta = %s, id_comprobante = %s, pais_destino = %s,
            descripcion_carga = %s, fecha_envio = %s
        WHERE id_exportacion = %s
    """
    cursor.execute(sql, (id_venta, id_comprobante, pais_destino, descripcion_carga, fecha_envio, id_exportacion))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_exportacion(id_exportacion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM exportaciones WHERE id_exportacion = %s", (id_exportacion,))
    conexion.commit()
    cursor.close()
    conexion.close()


