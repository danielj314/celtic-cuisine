from flask import render_template
from celticcuisine import app, db
from celticcuisine.models import Nations


@app.route("/")
def home():
    return render_template("base.html")
