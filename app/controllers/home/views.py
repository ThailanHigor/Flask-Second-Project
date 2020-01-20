from . import home
from flask import render_template, flash, url_for, redirect
from app.models.Todo import Todo
from app.forms.auth import TodoForm

from flask_login import current_user
from app.models.Todo import Todo
from app import db



@home.route("/", methods=["GET", "POST"])
def index():
    todos = None
    form = TodoForm()

    if current_user.is_authenticated:
        todos = Todo.query.filter_by(user_id = current_user.id).all()

    if form.validate_on_submit():
        todo = Todo.query.filter_by(title=form.title.data).first()

        if todo is None:
            t = Todo()
            t.title = form.title.data
            t.user_id = current_user.id

            db.session.add(t)
            db.session.commit()
            flash("Task adicionada com sucesso")
            flash("success")
            return redirect(url_for('.index'))
        else:
            flash("Task já existe")
            flash("error")
            return redirect(url_for('.index'))
        
    return render_template("home.html", form = form, todos = todos)

@home.route('/task/delete/<int:id>', methods=["GET"])
def delete_task(id):
    todo = Todo.query.filter_by(id=id).first()

    if todo is not None:
        db.session.delete(todo)
        db.session.commit()
        flash("Task removida com sucesso")
        flash("success")

    flash("Task não encontrada")
    flash("error")

    return redirect(url_for('.index'))