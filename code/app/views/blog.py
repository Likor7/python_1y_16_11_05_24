from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user

from app.controllers import PostController
from app.forms import PostForm

blog_blueprint = Blueprint("blog", __name__, url_prefix="/blog")


# 1) Сторінка окремого посту
# 2) Фото до посту
# 3) Перекласти сайт на українську
# 4) Редагування/видалення постів користувачем !сьогодні
# 5) Сторінка контаків
# 6) Головна сторінка
# 7) Емейл трохи логіки додати

# ДЗ
# 1) Поле created_at в таблиці (моделі) Post переробити на DateTime
# 2) Додати до корситувача поле about String(500)
# 3) Сторінка профілю


@blog_blueprint.route("/", methods=["GET"])
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
    return render_template(
        "blog/create_edit_post.html",
        title="Створення посту",
        form=form,
        form_action=url_for("blog.add_post"),
    )


@blog_blueprint.route("/post/edit/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = PostController.get_post_by_id(post_id)
    if not post:
        flash("Post not found", "danger")
        return redirect(url_for("blog.index"))

    form = PostForm(obj=post)
    if form.validate_on_submit():
        PostController.update_post(post_id, form.title.data, form.content.data)
        flash("The post has been updated", "info")
        return redirect(url_for("blog.view_post", post_id=post_id))
    elif form.is_submitted():
        flash("The given data was invalid.", "danger")

    return render_template(
        "blog/create_edit_post.html",
        title="Редагування посту",
        form=form,
        form_action=url_for("blog.edit_post", post_id=post_id),
    )


@blog_blueprint.route("/post/<int:post_id>", methods=["GET"])
def view_post(post_id):
    post = PostController.get_post_by_id(post_id)  # NoneType
    if not post:
        flash("Post not found", "danger")
        return redirect(url_for("main.index"))
    return render_template("blog/view_post.html", title=post.title, post=post)


@blog_blueprint.route("/post/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    post = PostController.get_post_by_id(post_id)

    if not post or current_user.id != post.user_id:
        flash("Not found")
        return redirect(url_for("blog.index"), code=303)

    PostController.delete_post(post_id)

    flash(f"Post {post.title} has been deleted")
    return redirect(url_for("blog.index"), code=303)
