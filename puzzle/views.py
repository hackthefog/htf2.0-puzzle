from puzzle import app, calculation
from hashlib import sha256
from flask import render_template, redirect, url_for

# Views
@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')


@app.route('/start', methods=['GET'])
def start():
    return render_template('start.html')


@app.route('/bot-slack', methods=['GET'])
def slack():
    return render_template('slack.html')


@app.route('/found/sha256', methods=['GET'])
def shanum():
    return render_template('hash.html')


@app.route('/hash/sha256/<inputForHash>', methods=['GET'])
@app.route('/hash/SHA256/<inputForHash>', methods=['GET'])
def hash(inputForHash):
    # Solution is 'c8b2d3d370a696b3e473f85dca4437264ad6d2094c1a2e2329040bbb71086abe'
    if inputForHash.lower() == sha256('Rafael Cenzano'.encode('utf-8')).hexdigest():
        return render_template('layers.html')


@app.route('/backdoor', methods=['GET'])
def rotating():
    return render_template('rot.html')


@app.route('/HacktheFogisthebest', methods=['GET'])
def rotation():
    return render_template('imageData.html')


@app.route('/calculate/<inputCalculation>')
def calculatingHard(inputCalculation):
    # Soultion is '4756482337'
    if inputCalculation == calculation.calculation():
        return '<h1>Hello there</h1>'

# Error Handelers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
