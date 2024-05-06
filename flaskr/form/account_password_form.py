from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField
from wtforms.validators import DataRequired, InputRequired


class AccountPasswordForm(FlaskForm):
    old_password = PasswordField('Старый пароль:', validators=[InputRequired()])
    new_password = PasswordField('Новый пароль:', validators=[InputRequired()])
    new_password_again = PasswordField('Подтверждение нового пароля:', validators=[InputRequired()])
    submit = SubmitField('Изменить пароль')