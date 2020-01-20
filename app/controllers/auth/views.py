from flask import render_template, redirect, flash, url_for, request
from flask_login import login_required, login_user, logout_user

from app.forms.auth import LoginForm, RegisterForm
from app.models.User import User

from . import auth
from app import db

@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        print('entrei')
        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            next = request.args.get("next")

            if next is None or not next.starswith('/'):
                next = url_for("home.index")

            flash("Bem vindo " + user.name)
            flash("success")
            return redirect(next)
            
        else:
            flash("Erro ao logar")
            flash("error") 
    
    return render_template("auth/login.html", form = form)

@auth.route("/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    flash("Deslogado com sucesso")
    flash("success")
    return redirect(url_for("auth.login"))

@auth.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
      
        if user is None:
            u = User()
            u.name = form.name.data
            u.password = form.password.data
            u.email = form.email.data
            
            db.session.add(u)
            db.session.commit()
    
            flash("Registrado com sucesso")
            flash("success")
            return redirect(url_for("auth.login"))
        else:
            flash("E-mail já registrado")
            flash("error")
    
    return render_template("auth/register.html", form = form)
