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



def obtener_tipos():
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tipos")
    resultado = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(resultado)

def obtener_tipos_por_id(id):
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tipos WHERE id_tipo = %s", (id,))
    fila = cursor.fetchone()
    cursor.close()
    conn.close()
    if fila:
        return jsonify(fila)
    return jsonify({"mensaje": "Tipo no encontrado"}), 404

def crear_tipos(data):
    conn = obtener_conexion()
    cursor = conn.cursor()
    sql = "INSERT INTO tipos (nombre) VALUES (%s)"
    cursor.execute(sql, (data['nombre'],))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"mensaje": "Tipo creado correctamente"})

def actualizar_tipos(id, data):
    conn = obtener_conexion()
    cursor = conn.cursor()
    sql = "UPDATE tipos SET nombre=%s WHERE id_tipo = %s"
    cursor.execute(sql, (data['nombre'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"mensaje": "Tipo actualizado correctamente"})

def eliminar_tipos(id):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tipos WHERE id_tipo = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"mensaje": "Tipo eliminado correctamente"})
