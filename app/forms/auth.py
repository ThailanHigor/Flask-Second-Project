from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, Length, DataRequired


class LoginForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(),Email(), Length(0,60)])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Logar")

class RegisterForm(FlaskForm):
    name = StringField("Nome",  validators=[DataRequired(), Length(0,60)])
    email = StringField("E-mail", validators=[DataRequired(),Email(), Length(0,60)])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Cadastrar")

class TodoForm(FlaskForm):
    title = StringField("Title",  validators=[DataRequired(), Length(0,60)])
    submit = SubmitField("Cadastrar")


