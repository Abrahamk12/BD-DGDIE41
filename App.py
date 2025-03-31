#region importaciones
import os
from flask import *
from login import *
from funciones import *
from passlib.hash import sha256_crypt
#endregion

#region incializacion
app = Flask(__name__)
app.secret_key = "Moltres_3l_Gu4jolot3_M4cias"
#endregion

#region rutas
@app.context_processor
def handle_context():
    return dict(os=os)

@app.route("/")
@app.route("/")
def index():
    if request.method == "GET":
        return render_template("index.html")
    
@app.route("/login", methods = ["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        msg = ""
        return render_template("login.html", mensaje=msg)
    else:
        if request.method == "POST":
            # Obtén los valores del formulario
            usuario = request.form.get("usuario")  # Cambiado de 'nombre' a 'usuario'
            password_forma = request.form.get("password")  # Cambiado de 'contraseña' a 'password'

            if not usuario or not password_forma:
                msg = "Por favor, completa todos los campos."
                return render_template("login.html", mensaje=msg)

            # Verifica si el usuario existe
            c_usuario = comprobarUsuario()
            if usuario not in c_usuario:
                return redirect("/registro")

            # Obtén la contraseña de la base de datos
            user = comprobarUsuario(usuario)
            if usuario == user:
                password_db = getPassword(usuario)  # Contraseña guardada en la base de datos
                verificado = sha256_crypt.verify(password_forma, password_db)  # Compara contraseñas

                if verificado:
                    # Configura la sesión
                    session["nombre"] = usuario
                    session["logged_in"] = True

                    # Redirige al inicio o a la ruta anterior si existe
                    if "ruta" in session and session["ruta"]:
                        ruta = session["ruta"]
                        session["ruta"] = None
                        return redirect(ruta)
                    else:
                        return redirect("/")
                else:
                    msg = f"La contraseña para el usuario {usuario} no es correcta."
                    return render_template("login.html", mensaje=msg)

            msg = "Usuario no registrado."
            return render_template("login.html", mensaje=msg)

@app.route("/registro", methods = ["GET", "POST"])
@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "GET":
        return render_template("registro.html")
    else:
        if request.method == "POST":
            valor = request.form.get('enviar')  # Usa .get() para evitar errores si no existe
            if valor == 'Enviar':
                usuario = request.form.get('usuario')  # Captura el valor del campo "usuario"
                password = request.form.get('password')  # Captura el valor del campo "password"
                password = sha256_crypt.hash(password)  # Hashea la contraseña

                # Comprueba si el usuario ya existe
                c_usuario = comprobarUsuario()
                if usuario not in c_usuario:
                    registrarUsuario(usuario, password)
                    return redirect('/login')
                else:
                    return render_template("registro.html", mensaje="Usuario ya registrado")
            return render_template("registro.html", mensaje="Error en el registro")


#endregion

#region inciar programa
if __name__ == '__main__':
    app.run(debug=True)
#endregion