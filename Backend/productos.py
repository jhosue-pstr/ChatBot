from flask import Flask, request, jsonify
import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="infotel_db",
        port=3306
    )


def obtener_productos():
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos")
    resultado = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(resultado)

def obtener_productos_por_id(id):
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos WHERE id_producto = %s", (id,))
    fila = cursor.fetchone()
    cursor.close()
    conn.close()
    if fila:
        return jsonify(fila)
    return jsonify({"mensaje": "Producto no encontrado"}), 404

def crear_productos(data):
    conn = obtener_conexion()
    cursor = conn.cursor()
    sql = """
        INSERT INTO productos (nombre, descripcion, precio_unitario, id_categoria, id_tipo, id_proveedor)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (
        data['nombre'],
        data['descripcion'],
        data['precio_unitario'],
        data['id_categoria'],
        data['id_tipo'],
        data['id_proveedor']
    )
    cursor.execute(sql, valores)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"mensaje": "Producto creado correctamente"})

def actualizar_productos(id, data):
    conn = obtener_conexion()
    cursor = conn.cursor()
    sql = """
        UPDATE productos
        SET nombre=%s, descripcion=%s, precio_unitario=%s,
            id_categoria=%s, id_tipo=%s, id_proveedor=%s
        WHERE id_producto = %s
    """
    valores = (
        data['nombre'],
        data['descripcion'],
        data['precio_unitario'],
        data['id_categoria'],
        data['id_tipo'],
        data['id_proveedor'],
        id
    )
    cursor.execute(sql, valores)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"mensaje": "Producto actualizado correctamente"})

def eliminar_productos(id):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id_producto = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"mensaje": "Producto eliminado correctamente"})
