from flask import Flask, request, jsonify
import cliente

app = Flask(__name__)

@app.route('/')
def inicio():
    return "API Clientes - INFOTEL BUSINESS"

@app.route('/clientes', methods=['POST'])
def crear_cliente():
    data = request.json
    cliente.crear_cliente(data)
    return jsonify({"mensaje": "Cliente creado con éxito"}), 201

# READ AL
@app.route('/clientes', methods=['GET'])
def listar_clientes():
    resultado = cliente.listar_clientes()
    return jsonify(resultado)

# READ ONE
@app.route('/clientes/<int:id_cliente>', methods=['GET'])
def obtener_cliente(id_cliente):
    cliente_data = cliente.obtener_cliente_por_id(id_cliente)
    if cliente_data:
        return jsonify(cliente_data)
    else:
        return jsonify({"mensaje": "Cliente no encontrado"}), 404

# UPDATE
@app.route('/clientes/<int:id_cliente>', methods=['PUT'])
def actualizar_cliente(id_cliente):
    data = request.json
    cliente.actualizar_cliente(id_cliente, data)
    return jsonify({"mensaje": "Cliente actualizado correctamente"})

# DELETE
@app.route('/clientes/<int:id_cliente>', methods=['DELETE'])
def eliminar_cliente(id_cliente):
    cliente.eliminar_cliente(id_cliente)
    return jsonify({"mensaje": "Cliente eliminado correctamente"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
