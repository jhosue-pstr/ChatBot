import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="infotel_db",
        port=3306
    )

def crear_documento(id_pedido, tipo_documento, numero, fecha_emision, archivo_url):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        INSERT INTO documentos (id_pedido, tipo_documento, numero, fecha_emision, archivo_url)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (id_pedido, tipo_documento, numero, fecha_emision, archivo_url))
    conexion.commit()
    cursor.close()
    conexion.close()

def listar_documentos():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM documentos")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def obtener_documento(id_documento):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM documentos WHERE id_documento = %s", (id_documento,))
    documento = cursor.fetchone()
    cursor.close()
    conexion.close()
    return documento

def actualizar_documento(id_documento, id_pedido, tipo_documento, numero, fecha_emision, archivo_url):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        UPDATE documentos
        SET id_pedido = %s, tipo_documento = %s, numero = %s, fecha_emision = %s, archivo_url = %s
        WHERE id_documento = %s
    """
    cursor.execute(sql, (id_pedido, tipo_documento, numero, fecha_emision, archivo_url, id_documento))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_documento(id_documento):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM documentos WHERE id_documento = %s", (id_documento,))
    conexion.commit()
    cursor.close()
    conexion.close()
