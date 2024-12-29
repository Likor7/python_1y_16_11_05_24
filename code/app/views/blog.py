from flask import Blueprint, render_template, request

blog_blueprint = Blueprint("blog", __name__, url_prefix="/blog")


@blog_blueprint.route("/")
def index():
    return render_template("index.html", title="Блог", current_page=request.endpoint)
