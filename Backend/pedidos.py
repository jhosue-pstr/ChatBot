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
def obtener_pedidos():
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pedidos")
    resultado = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(resultado)

def obtener_pedidos_por_id(id):
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pedidos WHERE id_pedido = %s", (id,))
    fila = cursor.fetchone()
    cursor.close()
    conn.close()
    if fila:
        return jsonify(fila)
    return jsonify({"mensaje": "Pedido no encontrado"}), 404

def crear_pedidos(data):
    conn = obtener_conexion()
    cursor = conn.cursor()
    sql = "INSERT INTO pedidos (id_cliente, fecha_pedido, estado) VALUES (%s, %s, %s)"
    valores = (data['id_cliente'], data['fecha_pedido'], data['estado'])
    cursor.execute(sql, valores)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"mensaje": "Pedido creado correctamente"})

def actualizar_pedidos(id, data):
    conn = obtener_conexion()
    cursor = conn.cursor()
    sql = """
        UPDATE pedidos
        SET id_cliente=%s, fecha_pedido=%s, estado=%s
        WHERE id_pedido = %s
    """
    valores = (data['id_cliente'], data['fecha_pedido'], data['estado'], id)
    cursor.execute(sql, valores)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"mensaje": "Pedido actualizado correctamente"})

def eliminar_pedidos(id):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pedidos WHERE id_pedido = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"mensaje": "Pedido eliminado correctamente"})
