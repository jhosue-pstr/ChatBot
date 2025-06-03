import mysql.connector
from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

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
    INSERT INTO clientes (nombres, usuario, apellido_paterno, apellido_materno, contraseña, email, telefono, direccion, tipo_documento, nro_documento)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (
        data['nombres'],
        data['usuario'],
        data['apellido_paterno'],
        data['apellido_materno'],
        data['contraseña'], 
        data['email'],
        data['telefono'],
        data['direccion'],
        data['tipo_documento'],
        data['nro_documento']
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
        UPDATE clientes SET nombres = %s, usuario = %s, apellido_paterno = %s, apellido_materno = %s, contraseña = %s,
        email = %s, telefono = %s, direccion = %s, tipo_documento = %s, nro_documento = %s
        WHERE id_cliente = %s
    """
    cursor.execute(sql, (
        data['nombres'],
        data['usuario'],
        data['apellido_paterno'],
        data['apellido_materno'],
        data['contraseña'],
        data['email'],
        data['telefono'],
        data['direccion'],
        data['tipo_documento'],
        data['nro_documento'],
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
