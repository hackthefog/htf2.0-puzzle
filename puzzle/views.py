from puzzle import app
from hashlib import sha256
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

@app.route("/hash/<inputForHash>", methods=['GET'])
def hashing(inputForHash):
    if inputForHash.lower() == 'sha256':
        return render_template('hash.html')

@app.route("/hash/sha256/<inputForHash>", methods=['GET'])
def hashed(inputForHash):
    # Solution is 'c8b2d3d370a696b3e473f85dca4437264ad6d2094c1a2e2329040bbb71086abe'
    if inputForHash.lower() == hashlib.sha256('Rafael Cenzano'.encode('utf-8')).hexdigest():
        return render_template('hash.html')

# Error Handelers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
