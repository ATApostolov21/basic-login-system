# app.py

from flask import Flask, render_template, request, redirect, url_for
from business_logic import authenticate_user, create_user

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if authenticate_user(username, password):
        return f'<p class="welcome-message">Welcome, {username}!</p>'
    else:
        return '<p class="invalid-message">Invalid credentials. Please try again.</p>'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        create_user(username, password)
        return redirect(url_for('home'))

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
