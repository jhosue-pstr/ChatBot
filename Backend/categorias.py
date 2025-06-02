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


def obtener_categorias():
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM categorias")
    resultado = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(resultado)

def obtener_categorias_por_id(id):
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM categorias WHERE id_categoria = %s", (id,))
    fila = cursor.fetchone()
    cursor.close()
    conn.close()
    if fila:
        return jsonify(fila)
    return jsonify({"mensaje": "Categoría no encontrada"}), 404

def crear_categorias(data):
    conn = obtener_conexion()
    cursor = conn.cursor()
    sql = "INSERT INTO categorias (nombre) VALUES (%s)"
    cursor.execute(sql, (data['nombre'],))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"mensaje": "Categoría creada correctamente"})

def actualizar_categorias(id, data):
    conn = obtener_conexion()
    cursor = conn.cursor()
    sql = "UPDATE categorias SET nombre=%s WHERE id_categoria = %s"
    cursor.execute(sql, (data['nombre'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"mensaje": "Categoría actualizada correctamente"})

def eliminar_categorias(id):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM categorias WHERE id_categoria = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"mensaje": "Categoría eliminada correctamente"})
