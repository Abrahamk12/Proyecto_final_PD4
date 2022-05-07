from flask import Flask, redirect, render_template, request, session
from funciones import *
from login import *
from passlib.hash import sha256_crypt
import os

app = Flask(__name__)
app.secret_key = "Moltr3s_3l_Gu4jolot3_M4cías"
user_in_sesion = "invitado"
@app.context_processor
def handle_context():
    return dict(os=os)

@app.route("/")
def index():
    menu = {}
    if user_in_sesion != "invitado":
        return render_template("index.html", menu = menu)
    else:
        menu = {}
        return render_template("index.html", menu = menu)
    

@app.route('/login', methods=['GET','POST'])
@app.route('/login/', methods=['GET','POST'])
def login():
#"""
    if request.method == 'GET':
        msg = ''
        return render_template('login.html',mensaje=msg)

    else:
        if request.method == 'POST':
            usuario = request.form['usuario']
            user = get_usuario(usuario)
            if usuario == user:
                password_db = get_password(usuario) # password guardado
                password_forma = request.form['password'] #password presentado
                verificado = sha256_crypt.verify(password_forma,password_db)
                user_in_sesion = user
                if (verificado == True):
                    session['usuario'] = usuario
                    session['logged_in'] = True
                    incio(user_in_sesion)
                    if 'ruta' in session:
                        ruta = session['ruta']
                        session['ruta'] = None
                        return redirect(ruta)
                    else:
                        return redirect("/u_opciones")
                else:
                    msg = f'El password de {usuario} no corresponde'
                    return render_template('login.html',mensaje=msg)
            
#"""
@app.route('/login_t', methods=['GET','POST'])
@app.route('/login_t/', methods=['GET','POST'])
def login_t():
    if request.method == 'GET':
        msg = ''
        return render_template('login_t.html',mensaje=msg)

    else:
        if request.method == 'POST':
            usuario = request.form['usuario']
            a_user = get_t_usuario(usuario)
        else:
            if usuario == a_user:
                password_db = get_t_password(usuario) # password guardado
                password_forma = request.form['password'] #password presentado
                verificado = sha256_crypt.verify(password_forma,password_db)
                if (verificado == True):
                    session['usuario'] = usuario
                    session['logged_in'] = True
                    user_in_sesion = usuario
                    if 'ruta' in session:
                        ruta = session['ruta']
                        session['ruta'] = None
                        return redirect(ruta)
                    else:
                        roll = get_roll(usuario)
                        if roll == "admininstrador":
                            return redirect("/a_opciones")
                        if roll == "trabajador":
                            return redirect("/t_opciones")
                        if roll == "doctor":
                            return redirect("/d_opciones")
                        else:
                            return redirect("/u_opciones")

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
            c_usuario = comprobar_usuario()
            if usuario not in c_usuario:
                save_user(n_competo, usuario, password_cryp, direccion, celular)
                return redirect('/login')

@app.route('/a_new_user', methods=['GET','POST'])
@app.route('/a_new_user/', methods=['GET','POST'])
def a_new_user():
    if request.method == 'GET':
        menu = l_menu(user_in_sesion)
        return render_template('a_new_user.html',menu = menu)
    if request.method == 'POST':
        valor = request.form['enviar']
        if valor == 'Enviar':
            usuario = request.form['usuario']
            n_completo  = request.form['n_completo']
            roll  = request.form['roll']
            password = request.form['password']
            password_cryp = sha256_crypt.hash(password)
            c_usuario = comprobar_usuario()
            if usuario not in c_usuario:
                save_t_user(n_completo,usuario,password_cryp,roll)
                return render_template('/')

@app.route('/add_new_user_t', methods=['GET','POST'])
@app.route('/add_new_user_t/', methods=['GET','POST'])
def add_new_user_t():
    if request.method == 'GET':
        msg = ''
        return render_template('add_new_user_t.html',mensaje=msg)
    if request.method == 'POST':
        valor = request.form['enviar']
        if valor == 'Enviar':
            usuario = request.form['usuario']
            n_completo  = request.form['n_completo']
            roll  = request.form['roll']
            password = request.form['password']
            password_cryp = sha256_crypt.hash(password)
            c_usuario = comprobar_usuario()
            if usuario not in c_usuario:
                save_t_user(n_completo,usuario,password_cryp,roll)
                return render_template('/')

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
            c_us = comprobar_usuario()
            c_tus = comprobar_tusuario()
            if usuario not in c_us:
                return redirect("/new_user")
            if usuario in c_tus:
                password_cryp = sha256_crypt.hash(password)
                actualizar_t_password(usuario, password_cryp)
            else:
                actualizar_password(usuario, password)
                return redirect("/")
          
#Apartado Administrador
@app.route('/a_opciones', methods=['GET','POST'])
@app.route('/a_opciones/', methods=['GET','POST'])
def a_opciones():
    if request.method == 'GET':
        menu = l_menu(user_in_sesion)
        return render_template('a_opciones.html', menu = menu)
    if request.method == 'POST':
        print()

#Apartado trabajador
@app.route('/t_opciones', methods=['GET','POST'])
@app.route('/t_opciones/', methods=['GET','POST'])
def t_opciones():
    if request.method == 'GET':
        menu = l_menu(user_in_sesion)
        return render_template('a_opciones.html', menu = menu)
    if request.method == 'POST':
        print()

#Apartado Doctor
@app.route('/d_opciones', methods=['GET','POST'])
@app.route('/d_opciones/', methods=['GET','POST'])
def d_opciones():
    if request.method == 'GET':
        menu = l_menu(user_in_sesion)
        return render_template('d_opciones.html', menu = menu)
    if request.method == 'POST':
        print()

#Apartado Usuario
@app.route('/u_opciones', methods=['GET','POST'])
@app.route('/u_opciones/', methods=['GET','POST'])
def u_opciones():
    if request.method == 'GET':
        menu = {"Agendar cita":"/agendar_cita/", 
                "Cambiar cita":"/cambiar_cita/", 
                "Cancelar cita":"/cancelar_cita/", 
                "Ver citas":"/ver_citas/", 
                "Ver historial":"/u_vhistorial/", 
                "Cambiar contraseña":"/u_restart_p/"}
        return render_template('d_opciones.html', menu = menu)
    if request.method == 'POST':
        print()

@app.route('/u_restart_p', methods=['GET','POST'])
@app.route('/u_restart_p/', methods=['GET','POST'])
def u_restart_p():
    if request.method == 'GET':
        menu = {"Agendar cita":"/agendar_cita/", 
                "Cambiar cita":"/cambiar_cita/", 
                "Cancelar cita":"/cancelar_cita/", 
                "Ver citas":"/ver_citas/", 
                "Ver historial":"/u_vhistorial/", 
                "Cambiar contraseña":"/u_restart_p/"}
        return render_template('cambiar_p.html',menu = menu)
    if request.method == 'POST':
        valor = request.form['enviar']
        if valor == 'Enviar':
            usuario = request.form['usuario']
            password = request.form['password']
            actualizar_password(usuario, password)
            return redirect("/u_opciones")

@app.route('/ver_historial', methods=['GET','POST'])
@app.route('/ver_historial/', methods=['GET','POST'])
def ver_historial():
    if request.method == 'GET':
        menu = {"Agendar cita":"/agendar_cita/", 
                "Cambiar cita":"/cambiar_cita/", 
                "Cancelar cita":"/cancelar_cita/", 
                "Ver citas":"/ver_citas/", 
                "Ver historial":"/ver_historial/", 
                "Cambiar contraseña":"/u_restart_p/"}
        return render_template('ver_historial.html',menu = menu)

@app.route('/ver_citas', methods=['GET','POST'])
@app.route('/ver_citas/', methods=['GET','POST'])
def ver_citas():
    if request.method == 'GET':
        menu = {"Agendar cita":"/agendar_cita/", 
                "Cambiar cita":"/cambiar_cita/", 
                "Cancelar cita":"/cancelar_cita/", 
                "Ver citas":"/ver_citas/", 
                "Ver historial":"/ver_historial/", 
                "Cambiar contraseña":"/u_restart_p/"}
        return render_template('ver_citas.html',menu = menu)

@app.route('/cancelar_cita', methods=['GET','POST'])
@app.route('/cancelar_cita/', methods=['GET','POST'])
def cancelar_cita():
    if request.method == 'GET':
        menu = {"Agendar cita":"/agendar_cita/", 
                "Cambiar cita":"/cambiar_cita/", 
                "Cancelar cita":"/cancelar_cita/", 
                "Ver citas":"/ver_citas/", 
                "Ver historial":"/ver_historial/", 
                "Cambiar contraseña":"/u_restart_p/"}
        return render_template('cancelar_cita.html',menu = menu)

@app.route('/cambiar_cita', methods=['GET','POST'])
@app.route('/cambiar_cita/', methods=['GET','POST'])
def cambiar_cita():
    if request.method == 'GET':
        menu = {"Agendar cita":"/agendar_cita/", 
                "Cambiar cita":"/cambiar_cita/", 
                "Cancelar cita":"/cancelar_cita/", 
                "Ver citas":"/ver_citas/", 
                "Ver historial":"/ver_historial/", 
                "Cambiar contraseña":"/u_restart_p/"}
        return render_template('cambiar_cita.html',menu = menu)

@app.route('/agendar_cita', methods=['GET','POST'])
@app.route('/agendar_cita/', methods=['GET','POST'])
def agendar_cita():
    if request.method == 'GET':
        menu = {"Agendar cita":"/agendar_cita/", 
                "Cambiar cita":"/cambiar_cita/", 
                "Cancelar cita":"/cancelar_cita/", 
                "Ver citas":"/ver_citas/", 
                "Ver historial":"/ver_historial/", 
                "Cambiar contraseña":"/u_restart_p/"}
        return render_template('agendar_cita.html',menu = menu)

#Cerrar sesion
@app.route('/logout', methods=['GET'])
@app.route('/logout/', methods=['GET'])
def logout():
    if request.method == 'GET':
        session.clear()
        user_in_sesion = "invitado"
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
    #app.run()