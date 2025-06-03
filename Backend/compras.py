import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="infotel_db",
        port=3306
    )


def crear_compra(id_proveedor, fecha_compra, total, metodo_pago):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        INSERT INTO compras (id_proveedor, fecha_compra, total, metodo_pago)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (id_proveedor, fecha_compra, total, metodo_pago))
    conexion.commit()
    cursor.close()
    conexion.close()

def listar_compras():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM compras")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def obtener_compra(id_compra):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM compras WHERE id_compra = %s", (id_compra,))
    compra = cursor.fetchone()
    cursor.close()
    conexion.close()
    return compra

def actualizar_compra(id_compra, id_proveedor, fecha_compra, total, metodo_pago):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        UPDATE compras
        SET id_proveedor = %s, fecha_compra = %s, total = %s, metodo_pago = %s
        WHERE id_compra = %s
    """
    cursor.execute(sql, (id_proveedor, fecha_compra, total, metodo_pago, id_compra))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_compra(id_compra):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM compras WHERE id_compra = %s", (id_compra,))
    conexion.commit()
    cursor.close()
    conexion.close()
