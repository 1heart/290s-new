import os
from flask import Flask, render_template, request, redirect
import fireBaseFunctions

app = Flask(__name__)

@app.route('/home')
def home():
	return render_template('home.html', users=fireBaseFunctions.getQuestions())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/newQuestion', methods=['GET', 'POST'])
def newQuestion():
	if request.method == 'POST':
		sentQuestion = fireBaseFunctions.postQuestion(\
			title=request.form['title'],
			description=request.form['description'],
			upvotes=0,
			user=request.form['user'],
			soundcloudLink=request.form['link'])
		return redirect("/home")
	# else:
	return render_template('newQuestion.html')


@app.route('/html5question', methods=['GET', 'POST'])
def html5question():
	if request.method == 'POST':
		sentQuestion = fireBaseFunctions.postQuestion(\
			title=request.form['title'],
			description=request.form['description'],
			upvotes=0,
			user=request.form['user'],
			soundcloudLink=request.form['link'])
		return redirect("/home")
	# else:
	return render_template('html5question.html')
