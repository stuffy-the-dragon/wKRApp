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
