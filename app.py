from flask import Flask, render_template, request, session
from flask_mysqldb import MySQL, MySQLdb
from flask_session import Session
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PORT'] = 3307
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/pedidos")
def pedidos():
    return render_template("pedido.html")
    

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/presentacion")
def presentacion():
    return render_template("presentacion.html")

# ruta para cargar pedido
@app.route('/cargarPedidos', methods=['POST'])
def cargarPedidos():
    if  request.method == 'POST':
        dni = request.form['dni']
        nombre = request.form['nombre']
        direccion= request.form['direccion']
        celular= request.form['celular']
        tipoDePizza= request.form['tipoDePizza']
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO pedido (dni, nombre, direccion, celular, tipodepizza)
                    VALUES (%s, %s, %s, %s, %s)'''
                    , (dni,nombre,direccion,celular,tipoDePizza))
        
        mysql.connection.commit()
        
        return render_template('menu.html')
    
# cargamos los datos a la tabla
@app.route("/tabla")
def tabla():
    cur = mysql.connection.cursor() 
    cur.execute('SELECT * FROM pedido')
    tablas = cur.fetchall()

    cur.close()
    return render_template("tabla.html", tablas = tablas)



if __name__=="__main__":
    app.run(port=5021,debug=True)