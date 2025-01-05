from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user

from app.controllers import PostController
from app.forms import PostForm

blog_blueprint = Blueprint("blog", __name__, url_prefix="/blog")


# 1) Сторінка окремого посту
# 2) Фото до посту
# 3) Перекласти сайт на українську
# 4) Редагування постів користувачем
# 5) Сторінка котактаків
# 6) Головна сторінка
# 7) Емейл трохи логіки додати

# ДЗ
# 1) Поле created_at в таблиці (моделі) Post переробити на DateTime
# 2) Додати до корситувача поле about String(500)
# 3) Сторінка профілю


@blog_blueprint.route("/")
def index():
    posts = PostController.get_posts()
    return render_template(
        "blog/index.html", title="Блог", current_page=request.endpoint, posts=posts
    )


@blog_blueprint.route("/post", methods=["GET", "POST"])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        PostController.create_post(form.title.data, form.content.data, current_user.id)

        flash("The post has been created", "info")
        return redirect(url_for("blog.index"))
    elif form.is_submitted():
        flash("The given data was invalid.", "danger")
    return render_template("blog/add_post.html", title="Створення посту", form=form)
