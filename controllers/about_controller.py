from flask import Flask, render_template, redirect
from flask import Blueprint


# INDEX
# GET '/about'
@about_blueprint.route("/about")
def about():
    return render_template("about/index.html", about = about)