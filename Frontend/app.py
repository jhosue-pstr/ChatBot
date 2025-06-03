from flask import Flask, render_template, request, redirect, url_for, session
import requests
from flask_dance.contrib.google import make_google_blueprint, google
import os

app = Flask(__name__)
app.secret_key = 'clave_secreta'

API_CLIENTE_URL = 'http://localhost:5000'

google_bp = make_google_blueprint(
    client_id=os.environ.get('GOOGLE_OAUTH_CLIENT_ID'),
    client_secret=os.environ.get('GOOGLE_OAUTH_CLIENT_SECRET'),
    scope=["profile", "email"],
    redirect_url="/login/google/authorized"
)
app.register_blueprint(google_bp, url_prefix="/login")

@app.route('/')
def index():
    usuario = session.get('usuario')
    return render_template('principal.html', usuario=usuario)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    response = requests.post('http://localhost:5000/clientes/login', json={
        'usuario': username,
        'contraseña': password
    })

    if response.status_code == 200:
        cliente = response.json()
        session['usuario'] = cliente['usuario']
        return redirect(url_for('index'))
    else:
        return "Credenciales inválidas", 401

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    token = google_bp.token
    if token:
        del google_bp.token
    return redirect(url_for('index'))

@app.route('/login/google')
def login_google():
    if not google.authorized:
        return redirect(url_for("google.login")) 
    
    resp = google.get("/oauth2/v2/userinfo")
    if resp.ok:
        user_info = resp.json()
        session['usuario'] = user_info['email'] 
        return redirect(url_for('index'))
    return "No se pudo obtener información del usuario de Google", 400

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        if request.form['contraseña'] != request.form['confirmar_contrasena']:
            return "Error: Las contraseñas no coinciden.", 400

        data = {
            'nombres': request.form['nombres'],  
            'usuario': request.form['usuario'],
            'apellido_paterno': request.form['apellido_paterno'],
            'apellido_materno': request.form['apellido_materno'],
            'contraseña': request.form['contraseña'],
            'email': request.form['email'],
            'telefono': request.form['telefono'],
            'direccion': request.form['direccion'],
            'tipo_documento': request.form['tipo_documento'],
            'nro_documento': request.form['nro_documento']
        }

        try:
            response = requests.post(f'{API_CLIENTE_URL}/clientes', json=data)
            if response.status_code == 201:
                return redirect(url_for('index'))
            else:
                return f"Error al registrar: {response.text}", 400
        except Exception as e:
            return f"Error de conexión con el backend: {str(e)}", 500

    return render_template('registrar.html')

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')  


@app.route('/citas', methods=['POST'])
def enviar_cita():
    data = {
        "nombre": request.form['name'],
        "correo": request.form['email'],
        "telefono_principal": request.form['phone'],
        "telefono_secundario": request.form.get('phone_secondary', ''),
        "fecha_cita": request.form['date'],
        "servicio": request.form['department'],
        "persona_contacto": request.form['contact_person'],
        "mensaje": request.form.get('message', '')
    }

    try:
        response = requests.post(f'{API_CLIENTE_URL}/citas', json=data)
        if response.status_code == 201:
            return redirect(url_for('index'))
        else:
            return f"Error al agendar cita: {response.text}", 400
    except Exception as e:
        return f"Error de conexión con el backend: {str(e)}", 500


if __name__ == '__main__':
    app.run(debug=True, port=5001)
