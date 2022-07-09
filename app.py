from flask import Flask, render_template
import genface
import os

app = Flask(__name__)

#UPLOAD_FOLDER = 'static/images/'
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDERpip

@app.route('/')
def index():
    image = genface.gene()
    image.save('./static/face.jpg')
    return render_template("index.html")

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response