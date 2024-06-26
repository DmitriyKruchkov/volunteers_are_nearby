from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired
from form.custom_validators import file_ext_validator


# Класс формы для редактирования данных
class AccountEditForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    photo = FileField(validators=[file_ext_validator(ext=["jpeg", "png", "jpg"])])
    about = TextAreaField("Немного о себе")
    submit = SubmitField('Изменить данные')

    def auto_fill(self, current_user):
        # автозаполнение формы
        self.name.data = current_user.name
        self.surname.data = current_user.surname
        self.about.data = current_user.about
