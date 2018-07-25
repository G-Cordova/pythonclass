from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/hi')
def hi():
    return "Hi there!"

@app.route('/theweeknd')
def sameoldsong():
    return "You're the same old song"

@app.route('/whatsgood/<bruh>')
def say_hello(bruh):
    return 'Hello %s' % bruh

@app.route('/file')
def hey():
    return render_template('hello.html', name='Cam')

@app.route('/handle_request', methods=['POST'])
def print_name():
    name = request.form['name']
    return name                    