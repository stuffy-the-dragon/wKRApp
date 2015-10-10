from wKRApp import app
from flask import Flask, render_template, url_for, request, redirect
from ipdb import set_trace


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template('team.html')
    return render_template('signin.html')


@app.route('/kra', methods=['GET', 'POST'])
def kra():
    if request.method == 'POST':
        return render_template('kra.html')
    return render_template('kra.html')


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


@app.route('/user_roles', methods=['GET', 'POST'])
def user_roles():
    if request.method == 'POST':
        return render_template('user_roles.html')
    return render_template('user_roles.html')


@app.route('/workflow', methods=['GET', 'POST'])
def workflow():
    if request.method == 'POST':
        return render_template('workflow.html')
    return render_template('workflow.html')