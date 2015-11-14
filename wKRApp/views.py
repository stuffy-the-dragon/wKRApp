from wKRApp import app
from flask import Flask, render_template, url_for, request, redirect, session, flash
from ipdb import set_trace
from functools import wraps


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
            return render_template('admin.html')
        else:
            session['logged_in'] = True
            flash('You were just logged in')
            return render_template('team.html')
    return render_template('signin.html', error=error)

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

# THIS MAY BE A PROBLEM SINCE ANYONE CAN NAVIGATE TO THE ADMIN AND ALL TEMPLATES BELOW  WITHOUT A SIGNIN
@app.route('/admin')
@login_required
def admin():
    return render_template('admin.html')


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