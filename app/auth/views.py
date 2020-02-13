from flask import redirect, render_template, url_for, flash

from app import db
from app.forms import RegisterForm, LoginForm
from app.models import User
from flask_login import login_user, logout_user, login_required

from . import auth


@auth.route("/register", methods=["POST", "GET"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        u = User(
            form.name.data,
            form.email.data,
            form.password.data
        )

        db.session.add(u)
        db.session.commit()

        return redirect(url_for(".login"))

    return render_template("add_user.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        u = User.query.filter_by(email=form.email.data).first()

        if not u:
            flash("Suas credênciais estão inválidas!", "danger")
            return redirect(url_for(".login"))
        
        if not u.check_password(form.password.data):
            flash("Suas credênciais estão inválidas!", "danger")
            return redirect(url_for(".login"))

        login_user(u)
        return redirect(url_for("home.secret_page"))

    return render_template("login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for(".login"))