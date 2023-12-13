from flask import Blueprint, render_template, request
from models.contact import Contact
from utils.db import db


contacts = Blueprint("contacts", __name__)

@contacts.route("/")
def home():
    return render_template("index.html")

@contacts.route("/new", methods=["POST"])
def add_contact():
    fullname = request.form["fullname"]
    email = request.form["email"]
    phone = request.form["phone"]

    new_contact = Contact(fullname, email, phone)

    db.session.add(new_contact)
    db.session.commit()

    return "Saving a contacts"

@contacts.route("/update")
def update():
    return "Update a contacts"

@contacts.route("/delete")
def delete():
    return "Delete a contacts"