from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, FileField, SubmitField
from wtforms.validators import DataRequired
from .custom_validators import file_ext_validator


class AccountEditForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    photo = FileField(validators=[file_ext_validator(ext=["jpeg", "png", "jpg"])])
    about = TextAreaField("Немного о себе")
    submit = SubmitField('Изменить данные')