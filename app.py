# import module
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date,timedelta

import sqlite3
from models import User
import r_fondi
import utenti


# create the application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'segreto'

login_manager = LoginManager()
login_manager.init_app(app)

# define the homepage
@app.route('/')
def index():
  raccolte_db = r_fondi.tutte()
  return render_template('index.html', raccolte=raccolte_db)

@app.route('/about')
def about():
  return render_template('about.html')

#check_password_hash(utente_db['password'], utente_form['password']):
@app.route('/login', methods=['POST'])
def login():

  utente_form = request.form.to_dict()
  utente_db = utenti.get_user_by_email(utente_form['email'])
  if not utente_db or not utente_db['password'] == utente_form['password']: 
    flash("Non esiste l'utente")
    return redirect(url_for('index'))
  else:
    new = User(id=utente_db['id'], username=utente_db['username'], email=utente_db['email'], password=utente_db['password'])
    login_user(new, True)
    flash('Success!')

    return redirect(url_for('index'))

@login_manager.user_loader
def load_user(user_id):
  db_user = utenti.get_user_by_id(user_id)
  if db_user:
        # Crea un oggetto User utilizzando i dati recuperati dal database
    user = User(id=db_user['id'],
            username=db_user['username'],
            email=db_user['email'],
            password=db_user['password'])
        # Restituisci l'oggetto User
    return user
  else:
        # Se l'utente non esiste nel database, restituisci None
    return None
    