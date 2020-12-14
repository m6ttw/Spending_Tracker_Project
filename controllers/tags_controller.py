from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.tag import Tag
import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)

#index
@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all()
    return render_template("tags/index.html", tags = tags)

#new
@tags_blueprint.route("/tags/new")
def new_tag():
    return render_template("tags/new.html")


#create
@tags_blueprint.route("/tags", methods=["POST"])
def create_tag():
    name = request.form["name"]
    new_tag = Tag(name)
    tag_repository.save(new_tag)
    return redirect("/tags")


#edit
@tags_blueprint.route("/tags/<id>/edit")
def edit_tag(id):
    tag = tag_repository.select(id)
    return render_template('tags/edit.html', tag=tag)


#update
@tags_blueprint.route("/tags/<id>", methods=["POST"])
def update_tag(id):
    name = request.form["name"]
    tag = Tag(name, id)
    tag_repository.update(tag)
    return redirect("/tags")
