from puzzle import app
from flask import render_template, redirect, url_for

# Views
@app.route("/", methods=['GET'])
def index():
    return render_template('home.html')

@app.route("/start", methods=['GET'])
def start():
    return render_template('start.html')

@app.route("/bot-slack", methods=['GET'])
def slack():
    return render_template('slack.html')

@app.route("/hash", methods=['GET'])
def hashing():
    return render_template('hash.html')

# Error Handelers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
