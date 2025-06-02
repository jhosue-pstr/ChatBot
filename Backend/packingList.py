import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="infotel_db",
        port=3306
    )



def crear_packing_list(id_exportacion, id_importacion, fecha_packing, descripcion, cantidad_total, peso_total, volumen_total, inspeccionado_por, observaciones):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        INSERT INTO packing_list (id_exportacion, id_importacion, fecha_packing, descripcion, cantidad_total, peso_total, volumen_total, inspeccionado_por, observaciones)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (id_exportacion, id_importacion, fecha_packing, descripcion, cantidad_total, peso_total, volumen_total, inspeccionado_por, observaciones))
    conexion.commit()
    cursor.close()
    conexion.close()

def listar_packing_list():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM packing_list")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def obtener_packing_list(id_packing):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM packing_list WHERE id_packing = %s", (id_packing,))
    packing = cursor.fetchone()
    cursor.close()
    conexion.close()
    return packing

def actualizar_packing_list(id_packing, id_exportacion, id_importacion, fecha_packing, descripcion, cantidad_total, peso_total, volumen_total, inspeccionado_por, observaciones):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        UPDATE packing_list
        SET id_exportacion = %s, id_importacion = %s, fecha_packing = %s, descripcion = %s, cantidad_total = %s, peso_total = %s, volumen_total = %s, inspeccionado_por = %s, observaciones = %s
        WHERE id_packing = %s
    """
    cursor.execute(sql, (id_exportacion, id_importacion, fecha_packing, descripcion, cantidad_total, peso_total, volumen_total, inspeccionado_por, observaciones, id_packing))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_packing_list(id_packing):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM packing_list WHERE id_packing = %s", (id_packing,))
    conexion.commit()
    cursor.close()
    conexion.close()
