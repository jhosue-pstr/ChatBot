import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="infotel_db",
        port=3306
    )

# Crear una compra de cliente
def crear_compra_cliente(id_catalogo, cantidad, metodo_de_pago):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    # Obtener el precio del producto
    cursor.execute("SELECT precio FROM catalogo WHERE id_catalogo = %s", (id_catalogo,))
    producto = cursor.fetchone()
    
    if not producto:
        return {"mensaje": "Producto no encontrado"}
    
    precio_unitario = producto[0]
    total = cantidad * precio_unitario  # Calcular el total automáticamente

    sql = """
        INSERT INTO compras_cliente (id_catalogo, cantidad, metodo_de_pago, total)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (id_catalogo, cantidad, metodo_de_pago, total))
    conexion.commit()
    
    cursor.close()
    conexion.close()
    return {"mensaje": "Compra registrada con éxito"}

# Listar todas las compras de clientes
def listar_compras_cliente():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM compras_cliente")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

# Obtener detalles de una compra específica
def obtener_compra_cliente(id_compras):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM compras_cliente WHERE id_compras = %s", (id_compras,))
    compra = cursor.fetchone()
    cursor.close()
    conexion.close()
    return compra if compra else {"mensaje": "Compra no encontrada"}

# Actualizar una compra de cliente
def actualizar_compra_cliente(id_compras, cantidad, metodo_de_pago):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    # Obtener precio del producto para recalcular el total
    cursor.execute("SELECT id_catalogo FROM compras_cliente WHERE id_compras = %s", (id_compras,))
    resultado = cursor.fetchone()
    
    if not resultado:
        return {"mensaje": "Compra no encontrada"}
    
    id_catalogo = resultado[0]
    cursor.execute("SELECT precio FROM catalogo WHERE id_catalogo = %s", (id_catalogo,))
    precio_unitario = cursor.fetchone()[0]
    total = cantidad * precio_unitario  # Calcular nuevo total

    sql = """
        UPDATE compras_cliente
        SET cantidad = %s, metodo_de_pago = %s, total = %s
        WHERE id_compras = %s
    """
    cursor.execute(sql, (cantidad, metodo_de_pago, total, id_compras))
    conexion.commit()
    cursor.close()
    conexion.close()
    return {"mensaje": "Compra actualizada correctamente"}

# Eliminar una compra de cliente
def eliminar_compra_cliente(id_compras):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM compras_cliente WHERE id_compras = %s", (id_compras,))
    conexion.commit()
    cursor.close()
    conexion.close()
    return {"mensaje": "Compra eliminada correctamente"}
