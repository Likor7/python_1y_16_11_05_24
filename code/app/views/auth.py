from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user

from app.forms import SignInForm, SignUpForm
from app.models import User

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/sign-in", methods=["GET", "POST"])
def signin():
    form = SignInForm(request.form)
    if form.validate_on_submit():
        user = User.authenticate(form.user_email.data, form.password.data)
        if user:
            login_user(user)
            flash("SignIn successful.", "success")
            return redirect(url_for("main.index"))
        flash("Wrong email or password.", "danger")
    return render_template("auth/signin.html", form=form)


@auth_blueprint.route("/sign-out", methods=["GET"])
def signout():
    logout_user()
    flash("Sign Out successful.", "success")
    return redirect(url_for("main.index"))


@auth_blueprint.route("/sign-up", methods=["GET", "POST"])
def signup():
    form = SignUpForm(request.form)
    if form.validate_on_submit():
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data,
            password=form.password.data,
        )
        user.save()
        login_user(user)
        flash("Registration successful. You are logged in.", "success")
        return redirect(url_for("main.index"))
    elif form.is_submitted():
        flash("The given data was invalid.", "danger")
    return render_template("auth/signup.html", form=form)
