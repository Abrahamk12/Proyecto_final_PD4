from flask import Flask, redirect, render_template, request, session
from funciones import graba_diccionario, lee_diccionario_csv
from passlib.hash import sha256_crypt
import os

app = Flask(__name__)
archivo_usuarios = 'usuarios.csv'
diccionario_usuarios = lee_diccionario_csv(archivo_usuarios)

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
            #print(request.form.keys())
            usuario = request.form['usuario']
            if usuario in diccionario_usuarios:
                password_db = diccionario_usuarios[usuario]['password'] # password guardado
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
            else:
                msg = f'usuario {usuario} no existe'
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
                    usuario =  request.form['usuario']
                    n_competo  =  request.form['n_competo']
                    direccion    =  request.form['direccion']
                    celular  =   request.form['celular']
                    password  =   request.form['password']
                    password_cryp = sha256_crypt.hash(password)
                    id = print()
                    if usuario not in diccionario_usuarios:
                        diccionario_usuarios[usuario] = {
                            #'id' : id,
                            'usuario': usuario,
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

@app.route('/logout', methods=['GET'])
@app.route('/logout/', methods=['GET'])
def logout():
    if request.method == 'GET':
        session.clear()
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)