from flask import Flask, redirect, render_template, request, session
from funciones import graba_diccionario, lee_diccionario_csv, cambiar_clave
from passlib.hash import sha256_crypt
import os

app = Flask(__name__)
app.secret_key = "Moltr3s_3l_Gu4jolot3_M4cías"
archivo_usuarios = 'usuarios.csv'
archivo_usuarios_a = 'a_usuarios.csv'
citas = 'citas.csv'
d_citas = lee_diccionario_csv(citas)
diccionario_usuarios = lee_diccionario_csv(archivo_usuarios)
diccionario_usuarios_a = lee_diccionario_csv(archivo_usuarios_a)

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
            if usuario in diccionario_usuarios:
                password_db = diccionario_usuarios[usuario]['password'] # password guardado
                password_forma = request.form['password'] #password presentado
                verificado = sha256_crypt.verify(password_forma,password_db)
                #"""
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
                #"""
            if usuario in diccionario_usuarios_a:
                password_db = diccionario_usuarios_a[usuario]['password'] # password guardad
                password_forma = request.form['password'] #password presentado
                password_db_crip = sha256_crypt.hash(password_db)
                password_db = diccionario_usuarios_a[usuario]['password'] # password guardad
                verificado = sha256_crypt.verify(password_forma,password_db_crip)
                #"""
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
                        roll = diccionario_usuarios_a[usuario]['roll']
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
            if usuario not in diccionario_usuarios:
                diccionario_usuarios[usuario] = {
                    'password': password_cryp,
                    'n_competo'  : n_competo,
                    'direccion': direccion,
                    'celular': celular
                }
            graba_diccionario(diccionario_usuarios,'usuario',archivo_usuarios)
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
            direccion = request.form['direccion']
            celular = request.form['celular']
            password = request.form['password']
            password_cryp = sha256_crypt.hash(password)
            if usuario not in diccionario_usuarios:
                diccionario_usuarios[usuario] = {
                    'id' : id,
                    'password': password_cryp,
                    'n_competo'  : n_competo,
                    'direccion': direccion,
                    'celular': celular
                }
            graba_diccionario(diccionario_usuarios,'usuario',archivo_usuarios)

@app.route('/restart_password', methods=['GET','POST'])
@app.route('/restart_password/', methods=['GET','POST'])
def restart_password():
    if request.method == 'GET':
        msg = ''
        return render_template('restart_password.html',mensaje=msg)
    if request.method == 'POST':
        valor = request.form['enviar']
        if valor == 'enviar':
            if usuario in diccionario_usuarios:
                usuario = request.form['usuario']
                password = request.form['password']
                print("La nueva cotraseña es: ",diccionario_usuarios,"\n")
                cambiar_clave(usuario,password,archivo_usuarios)
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