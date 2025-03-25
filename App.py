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
    
@app.route("/login")
@app.route("/login")
def login():
    if request.method == "GET":
        msg = ""
        return render_template("login.html", mensaje=msg)
    else:
        if request.method == "POST":
            usuario = request.form['usuario']
            user = comprobarUsuario(usuario)
            c_usuario = comprobarUsuario()
            if usuario not in c_usuario:
                return redirect('/registro')
            else:
                if usuario == user:
                    password_db = getPassword(usuario)#password guardado en la base de datos
                    password_forma = request.form["password"]#password presentado
                    verificado = sha256_crypt.verify(password_forma, password_db)
                    user_in_sesion = usuario
                    if verificado == True:
                        session['nombre'] = usuario
                        session['logged_in'] = True
                        inicio(user_in_sesion)
                        if 'ruta' in session:
                            ruta = session['ruta']
                            session['ruta'] = None
                            return redirect(ruta)
                        else:
                            return redirect('/')
#endregion

#region inciar programa
if __name__ == '__main__':
    app.run(debug=True)
#endregion