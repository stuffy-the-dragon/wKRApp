from wKRApp import app
from flask import Flask, render_template, url_for, request, redirect
from ipdb import set_trace

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'Admin' or request.form['password'] == 'admin':
            return render_template('admin.html')
        else:
            return render_template('team.html')
    return render_template('signin.html')


@app.route('/kra', methods=['GET', 'POST'])
def kra():
    if request.method == 'POST':
        return render_template('kra.html')
    return render_template('kra.html')

# THIS MAY BE A PROBLEM SINCE ANYONE CAN NAVIGATE TO THE ADMIN AND ALL TEMPLATES BELOW  WITHOUT A SIGNIN
@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/users')
def users():
    return render_template('users.html')


@app.route('/user_roles')
def user_roles():
    return render_template('user_roles.html')


@app.route('/workflow')
def workflow():
    return render_template('workflow.html')


@app.route('/career_ladders')
def career_ladders():
    return render_template('career_ladders.html')


@app.route('/new_role', methods=['GET', 'POST'])
def new_role():
    if request.method == 'POST':
        return render_template('new_role.html')
    return render_template('new_role.html')

@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        return render_template('new_user.html')
    return render_template('new_user.html')