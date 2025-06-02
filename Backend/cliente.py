import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="infotel_db",
        port=3306
    )

def crear_cliente(data):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        INSERT INTO clientes (nombre, tipo_documento, nro_documento, direccion, telefono, email)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (
        data['nombre'],
        data['tipo_documento'],
        data['nro_documento'],
        data['direccion'],
        data['telefono'],
        data['email']
    ))
    conexion.commit()
    cursor.close()
    conexion.close()

def listar_clientes():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    resultado = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultado

def obtener_cliente_por_id(id_cliente):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes WHERE id_cliente = %s", (id_cliente,))
    cliente = cursor.fetchone()
    cursor.close()
    conexion.close()
    return cliente

def actualizar_cliente(id_cliente, data):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        UPDATE clientes SET nombre = %s, tipo_documento = %s, nro_documento = %s,
        direccion = %s, telefono = %s, email = %s WHERE id_cliente = %s
    """
    cursor.execute(sql, (
        data['nombre'],
        data['tipo_documento'],
        data['nro_documento'],
        data['direccion'],
        data['telefono'],
        data['email'],
        id_cliente
    ))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_cliente(id_cliente):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM clientes WHERE id_cliente = %s", (id_cliente,))
    conexion.commit()
    cursor.close()
    conexion.close()
