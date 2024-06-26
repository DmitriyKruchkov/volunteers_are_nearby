from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, FileField
from wtforms.validators import DataRequired
from form.custom_validators import file_ext_validator


# Класс формы для регистрации
class RegisterForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    nickname = StringField('Никнейм', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    photo = FileField(validators=[file_ext_validator(ext=["jpeg", "png", "jpg"])])
    about = TextAreaField("Немного о себе")
    submit = SubmitField('Войти')
