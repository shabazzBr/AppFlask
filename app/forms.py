from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, Length


class RegisterForm(Form):
    name = StringField("Nome", validators=[
        DataRequired("campo obrigatório"),
        Length(5, 100, "o campo deve possuir entre 05 a 100 carácters")
    ])
    email = StringField("E-mail", validators=[
        DataRequired("campo obrigatório"),
        Email('não é um e-mail válido'),
        Length(5, 84, "o campo deve possuir entre 05 a 100 carácters")
    ])
    password = PasswordField("Senha", validators=[
        DataRequired("campo obrigatório")
    ])
    
    submit = SubmitField("Cadastrar")

class LoginForm(Form):
    email = StringField("E-mail", validators=[
        DataRequired("campo obrigatório"),
        Email('não é um e-mail válido')
    ])
    password = PasswordField("Senha", validators=[
        DataRequired("campo obrigatório")
    ])
    
    submit = SubmitField("Entrar")

