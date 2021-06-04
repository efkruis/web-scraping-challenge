#importing libraries
from flask import Flask, render_template
from flask_pymongo import PyMongo


#@ TODO: Intialize flas app
app = Flask(__name__)

# @TODO: creating a route and view function that takes in a string 
# and renders index.html template
@app.route("/")
def index():
    return render_template("index.html")