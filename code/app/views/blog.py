from flask import Blueprint, render_template, request

blog_blueprint = Blueprint("blog", __name__, url_prefix="/blog")


@blog_blueprint.route("/")
def index():
    return render_template(
        "blog/index.html", title="Блог", current_page=request.endpoint
    )


@blog_blueprint.route("/post")
def add_post():
    return render_template(
        "blog/add_post.html", title="Додати пост", current_page=request.endpoint
    )
