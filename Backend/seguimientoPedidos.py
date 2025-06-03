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

def crear_seguimiento(data):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        INSERT INTO seguimiento_pedidos (id_pedido, fecha_actualizacion, estado, observaciones)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (
        data['id_pedido'],
        data['fecha_actualizacion'],
        data['estado'],
        data['observaciones']
    ))
    conexion.commit()
    cursor.close()
    conexion.close()

def listar_seguimiento():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM seguimiento_pedidos")
    resultado = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultado

def obtener_seguimiento_por_id(id_seguimiento):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM seguimiento_pedidos WHERE id_seguimiento = %s", (id_seguimiento,))
    registro = cursor.fetchone()
    cursor.close()
    conexion.close()
    return registro

def actualizar_seguimiento(id_seguimiento, data):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        UPDATE seguimiento_pedidos SET id_pedido=%s, fecha_actualizacion=%s, estado=%s, observaciones=%s
        WHERE id_seguimiento=%s
    """
    cursor.execute(sql, (
        data['id_pedido'],
        data['fecha_actualizacion'],
        data['estado'],
        data['observaciones'],
        id_seguimiento
    ))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_seguimiento(id_seguimiento):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM seguimiento_pedidos WHERE id_seguimiento = %s", (id_seguimiento,))
    conexion.commit()
    cursor.close()
    conexion.close()
