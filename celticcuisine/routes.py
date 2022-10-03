from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from celticcuisine import app, db, mongo
from celticcuisine.models import Nations


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)
