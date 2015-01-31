import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
	return render_template('home')

@app.route('/')
def index():
    return render_template('index.html')
