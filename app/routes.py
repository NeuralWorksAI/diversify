from app import app
from app.forms import LoginForm, RegisterForm
from flask import render_template, session, request, redirect, url_for, flash, jsonify
from os import getenv
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

myclient = MongoClient(getenv("MONGO_URI"))
mydb = myclient["diversify"]

def assignSession(username):
    session["username"] = username

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form=LoginForm()
    if form.validate_on_submit():
        user = mydb.users.find_one({'username': form.username.data})
        if user and user['password'] == form.password.data:
            assignSession(user['username'])
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
    return render_template("signin.html", form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form=RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        confirmPassword = form.confirmPassword.data
        if password != confirmPassword:
            flash('Passwords do not match')
            return redirect(url_for('signup'))
        if mydb.users.find_one({'username': username}):
            flash('Username already taken')
            return redirect(url_for('signup'))
        mydb.users.insert_one({"username": username, "email": email, "password": password})
        assignSession(username)
        return redirect(url_for('dashboard'))
    return render_template("signup.html", form=form)

@app.route("/dashboard")
def dashboard():
    if not 'username' in session:
        return redirect(url_for('signin'))
    elif not 'formComplete' in session:
        return redirect(url_for('startform'))
    return render_template("dashboard.html", session=session)

@app.route("/form/start")
def startform():
    return render_template("startform.html", session=session)