from flask import Flask, render_template, redirect
from flask import Blueprint


# INDEX
# GET '/contact'
@contact_blueprint.route("/contact")
def contact():
    return render_template("contact/index.html", contact = contact)