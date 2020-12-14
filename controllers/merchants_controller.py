from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint("merchants", __name__)

#index
@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchants/index.html", merchants = merchants)

#new
@merchants_blueprint.route("/merchants/new")
def new_merchant():
    return render_template("merchants/new.html")


#create
@merchants_blueprint.route("/merchants", methods=["POST"])
def create_merchant():
    name = request.form["name"]
    new_merchant = Merchant(name)
    merchant_repository.save(new_merchant)
    return redirect("/merchants")


#edit
@merchants_blueprint.route("/merchants/<id>/edit")
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template('merchants/edit.html', merchant=merchant)


#update
@merchants_blueprint.route("/merchants/<id>", methods=["POST"])
def update_merchant(id):
    name = request.form["name"]
    merchant = Merchant(name, id)
    merchant_repository.update(merchant)
    return redirect("/merchants")
