from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from PythonResources.UsuariosDAO import UsuariosDAO

app = Flask(__name__)


@app.route('/')
def home():
    nombre = "Luis Gerardo Valencia Camacho"
    ticks = datetime.now()
    data = UsuariosDAO.guardarUsuario()
    return render_template("index.html", contacts=data, fecha=ticks, nombre=nombre) 


@app.route('/Usuarios', methods=['POST'])
def doPost():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        fechaNacimiento = request.form['fechaNacimiento']
        genero = request.form['genero']
        resultado = UsuariosDAO.guardarUsuario(nombre, apellidos, fechaNacimiento, genero)
        if resultado == 1:
            print("Usuario guardado")
        else:
            print("Error al guardar el usuario")
    else:
        print("ERROR")

    return redirect(url_for("home"))

@app.route('/borrar-usuario/<string:id>')
def borrarUsuario(id):
    UsuariosDAO.guardarUsuario(None, None, None, None, id)
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(port=5000, debug=True)
