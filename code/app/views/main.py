from flask import Blueprint, render_template, request

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def index():
    return render_template("index.html", title="Головна", current_page=request.endpoint)


@main_blueprint.route("/contacts")
def contacts():
    return render_template(
        "index.html", title="Контакти", current_page=request.endpoint
    )
