📱 Infotel

Proyecto que incluye backend, frontend y un bot de WhatsApp. Sigue los pasos a continuación para levantar correctamente cada componente del sistema.
🧠 Requisitos Previos

    Python 3.x

    Node.js v20 o superior

    npm (Node Package Manager)

    MySQL o MariaDB

🚀 Instalación del Proyecto
1. Clonar el Repositorio

git clone https://github.com/jhosue-pstr/Infotel.git
cd Infotel

2. Importar la Base de Datos

Importa el archivo .sql ubicado en la carpeta backend a tu gestor de base de datos (MySQL o MariaDB).
3. Crear un Entorno Virtual en Python

python3 -m venv venv

4. Activar el Entorno Virtual

    En Linux/macOS:

source venv/bin/activate

En Windows:

    venv\Scripts\activate

5. Instalar las Dependencias del Backend

cd backend
pip install -r requeriments.txt

6. Ejecutar el Backend

python3 app.py

El servidor debería iniciarse en el puerto 5000.
🌐 Levantar el Frontend
7. En una Nueva Terminal

    Activa nuevamente el entorno virtual:

source venv/bin/activate

Luego entra a la carpeta del frontend y ejecuta:

    cd ../frontend
    python3 app.py

El frontend debería estar corriendo en el puerto 5001.
8. Abrir en el Navegador

Abre tu navegador en la siguiente URL:

http://127.0.0.1:5001

🤖 Crear el Bot de WhatsApp
Requisitos

    Tener instalado npm y node (versión 20 o superior).

Pasos

    Desde la raíz del proyecto, ejecuta en la terminal:

    npm create bot-whatsapp@latest

    Sigue estas instrucciones cuando se te pregunte:

        Selecciona Sí cuando te pida continuar.

        Elige Baileys como proveedor de conexión.

        Elige Memory como adaptador de base de datos.

✅ ¡Listo!

Ya tienes funcionando el backend, el frontend y el bot de WhatsApp de Infotel. 🚀
