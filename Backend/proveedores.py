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

def obtener_proveedores():
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM proveedores")
    resultado = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(resultado)

def obtener_proveedores_por_id(id):
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM proveedores WHERE id_proveedor = %s", (id,))
    fila = cursor.fetchone()
    cursor.close()
    conn.close()
    if fila:
        return jsonify(fila)
    return jsonify({"mensaje": "Proveedor no encontrado"}), 404

def crear_proveedores(data):
    conn = obtener_conexion()
    cursor = conn.cursor()
    sql = "INSERT INTO proveedores (nombre, contacto, direccion) VALUES (%s, %s, %s)"
    valores = (data['nombre'], data['contacto'], data['direccion'])
    cursor.execute(sql, valores)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"mensaje": "Proveedor creado correctamente"})

def actualizar_proveedores(id, data):
    conn = obtener_conexion()
    cursor = conn.cursor()
    sql = """
        UPDATE proveedores SET nombre=%s, contacto=%s, direccion=%s
        WHERE id_proveedor = %s
    """
    valores = (data['nombre'], data['contacto'], data['direccion'], id)
    cursor.execute(sql, valores)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"mensaje": "Proveedor actualizado correctamente"})

def eliminar_proveedores(id):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM proveedores WHERE id_proveedor = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"mensaje": "Proveedor eliminado correctamente"})
