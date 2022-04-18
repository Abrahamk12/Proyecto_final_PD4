from flask import Flask, redirect, render_template, request, session
from funciones import *
from passlib.hash import sha256_crypt
import os

app = Flask(__name__)
app.secret_key = "Moltr3s_3l_Gu4jolot3_M4cías"

@app.context_processor
def handle_context():
    return dict(os=os)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET','POST'])
@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        msg = ''
        return render_template('login.html',mensaje=msg)
    #"""
    else:
        if request.method == 'POST':
            usuario = request.form['usuario']
            user = get_usuario(usuario)
            print("\nEste es el usuario perra: ", user, "\n")
            if usuario == user:
                password_db = get_password(usuario) # password guardado
                print("\nEste es el la contraseña perra: ", user, "\n")
                password_forma = request.form['password'] #password presentado
                verificado = sha256_crypt.verify(password_forma,password_db)
                if (verificado == True):
                    session['usuario'] = usuario
                    session['logged_in'] = True
                    if 'ruta' in session:
                        ruta = session['ruta']
                        session['ruta'] = None
                        return redirect(ruta)
                    else:
                        return redirect("/")
                else:
                    msg = f'El password de {usuario} no corresponde'
                    return render_template('login.html',mensaje=msg)
            a_user = get_t_usuario(usuario)
            if usuario == a_user:
                password_db = get_t_password(usuario) # password guardado
                password_forma = request.form['password'] #password presentado
                verificado = sha256_crypt.verify(password_forma,password_db)
                if (verificado == True):
                    session['usuario'] = usuario
                    session['logged_in'] = True
                    if 'ruta' in session:
                        ruta = session['ruta']
                        session['ruta'] = None
                        return redirect(ruta)
                    else:
                        #El chiste es ver si es un admin o un trabajador, dependiendo de que lo mande a la pag
                        #no se me ocurre como hacerlo :v
                        roll = get_roll(usuario)
                        if roll == "admin":
                            return redirect("/a_opciones")
                        if roll == "trabajador":
                            return redirect("/t_opciones")
                        else:
                            return redirect("/")
                else:
                    msg = f'El password de {usuario} no corresponde'
                    return render_template('login.html',mensaje=msg)
    #"""

@app.route('/new_user', methods=['GET','POST'])
@app.route('/new_user/', methods=['GET','POST'])
def new_user():
    if request.method == 'GET':
        msg = ''
        return render_template('new_user.html',mensaje=msg)
    if request.method == 'POST':
        valor = request.form['enviar']
        if valor == 'Enviar':
            usuario = request.form['usuario']
            n_competo  = request.form['n_competo']
            direccion = request.form['direccion']
            celular = request.form['celular']
            password = request.form['password']
            password_cryp = sha256_crypt.hash(password)
            save_user(n_competo, usuario, password_cryp, direccion, celular)
        return redirect('/')

@app.route('/a_new_user', methods=['GET','POST'])
@app.route('/a_new_user/', methods=['GET','POST'])
def a_new_user():
    if request.method == 'GET':
        msg = ''
        return render_template('a_new_user.html',mensaje=msg)
    if request.method == 'POST':
        valor = request.form['enviar']
        if valor == 'Enviar':
            usuario = request.form['usuario']
            n_competo  = request.form['n_competo']
            roll  = request.form['roll']
            password = request.form['password']
            password_cryp = sha256_crypt.hash(password)
            save_t_user(n_competo,usuario,password_cryp,roll)

@app.route('/restart_password', methods=['GET','POST'])
@app.route('/restart_password/', methods=['GET','POST'])
def restart_password():
    if request.method == 'GET':
        msg = ''
        return render_template('restart_password.html',mensaje=msg)
    if request.method == 'POST':
        valor = request.form['enviar']
        if valor == 'Enviar':
            usuario = request.form['usuario']
            password = request.form['password']
            user = get_usuario(usuario)
            if usuario == user:
                actualizar_password(usuario, password)
                return redirect("/")

@app.route('/a_opciones', methods=['GET','POST'])
@app.route('/a_opciones/', methods=['GET','POST'])
def a_opciones():
    if request.method == 'GET':
        msg = ''
        return render_template('a_opciones.html',mensaje=msg)
    if request.method == 'POST':
        print()

@app.route('/logout', methods=['GET'])
@app.route('/logout/', methods=['GET'])
def logout():
    if request.method == 'GET':
        session.clear()
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)