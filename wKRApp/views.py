from wKRApp import app
from flask import Flask, render_template, url_for, request, redirect, session, flash, g
from ipdb import set_trace
from functools import wraps
import sqlite3
import os.path

 # 2 security flaws, need to sort out
 #      1. the key should be randomy generated
 #      2. the key should be set in a config file that is then imported in.
app.secret_key = "my precious"
app.database = "sample.db"


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('index'))
    return wrap


@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'Admin' or request.form['password'] == 'admin':
            session['logged_in'] = True
            flash('You were just logged in')
            return redirect(url_for('admin'))
        else:
            session['logged_in'] = True
            flash('You were just logged in')
            return redirect(url_for('team'))
    return render_template('signin.html', error=error)



@app.route('/team')
@login_required
def team():
    return render_template('team.html')

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None) 
    flash('You were just logged out')
    return redirect(url_for('index'))

@app.route('/kra', methods=['GET', 'POST'])
@login_required
def kra():
    if request.method == 'POST':
        return render_template('kra.html')
    return render_template('kra.html')


@app.route('/admin')
@login_required
def admin():
    g.db = connect_db()
    db_object = g.db
    cur = db_object.execute('SELECT * from posts')
    posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('admin.html', posts=posts)


@app.route('/users')
@login_required
def users():
    return render_template('users.html')


@app.route('/user_roles')
@login_required
def user_roles():
    return render_template('user_roles.html')


@app.route('/workflow')
@login_required
def workflow():
    return render_template('workflow.html')


@app.route('/career_ladders')
@login_required
def career_ladders():
    return render_template('career_ladders.html')


@app.route('/new_role', methods=['GET', 'POST'])
@login_required
def new_role():
    if request.method == 'POST':
        return render_template('new_role.html')
    return render_template('new_role.html')

@app.route('/new_user', methods=['GET', 'POST'])
@login_required
def new_user():
    if request.method == 'POST':
        return render_template('new_user.html')
    return render_template('new_user.html')



def connect_db():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR + os.path.sep + 'db', app.database)
    return sqlite3.connect(db_path)

