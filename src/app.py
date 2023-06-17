import numpy as np
from flask import Flask,request,jsonify,render_template


# Initialize the app
app = Flask(__name__)

@app.route('/')
def home_page():
    return 'Hello World'

# @app.route('/images')
# def images():
#     return 'sample page for images'

app.run()