from flask import Flask, render_template, send_from_directory
import mysql.connector
import os

app = Flask(__name__,
            template_folder='html',  # Ruta para archivos HTML
            static_folder='')  # Sin usar la carpeta 'static'

# Conexión a la base de datos MySQL
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',  # Cambia el usuario si es necesario
        password='',  # Cambia la contraseña si es necesario
        database='remanfast'
    )
    return conn

# Ruta para la página principal (INDEX)
@app.route('/')
def index():
    return render_template('index.html')  # Flask buscará en /html/index.html

# Ruta para recofiltro.html con consulta a la base de datos
@app.route('/html')
def html():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos LIMIT 4")
    productos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('accesorios.html', productos=productos)

# Ruta para la página de un producto
@app.route('/producto/<imagen>')
def producto(imagen):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Cambiar la consulta para que utilice LIKE
    cursor.execute("SELECT * FROM productos WHERE imagen LIKE %s", ('%' + imagen + '%',))  # Usamos LIKE para coincidencias parciales
    producto = cursor.fetchone()
    cursor.close()

    if producto is None:
        return "Producto no encontrado", 404  # Si no se encuentra el producto, devuelve un 404

    # Obtener productos recomendados basados en la categoría del producto
    productos_recomendados = obtener_productos_recomendados(producto['id'])
    return render_template('producto.html', producto=producto, productos_recomendados=productos_recomendados)


# Función para obtener productos recomendados
def obtener_productos_recomendados(producto_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos WHERE categoria = (SELECT categoria FROM productos WHERE id = %s)", (producto_id,))
    productos_recomendados = cursor.fetchall()
    cursor.close()
    conn.close()
    return productos_recomendados

# Ruta para archivos CSS
@app.route('/css/<filename>')
def css(filename):
    return send_from_directory('css', filename)  # Servir archivos desde /css/

# Ruta para archivos JS
@app.route('/js/<filename>')
def js(filename):
    return send_from_directory('js', filename)  # Servir archivos desde /js/

# Ruta para imágenes
@app.route('/img/<filename>')
def img(filename):
    return send_from_directory('img', filename)  # Servir imágenes desde /img/

@app.route('/accesorios')
def accesorios():
    return render_template('accesorios.html')

@app.route('/recofiltro')
def recofiltro():
    return render_template('recofiltro.html')

@app.route('/recorueda')
def recorueda():
    return render_template('recorueda.html')

@app.route('/recofundas')
def recofundas():
    return render_template('recofundas.html')

@app.route('/recomangueras')
def recomangueras():
    return render_template('recomangueras.html')

if __name__ == '__main__':
    app.run(debug=True)
