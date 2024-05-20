from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FileField, SelectField, \
    DateTimeLocalField
from wtforms.validators import DataRequired
from form.custom_validators import file_ext_validator


class SuggestedEventForm(FlaskForm):
    id_event_type = SelectField('Тип события')
    event_name = StringField('Название события', validators=[DataRequired()])
    date_of_start = DateTimeLocalField('Дата начала', format="%Y-%m-%dT%H:%M", validators=[DataRequired()])
    address = StringField('Местоположение', validators=[DataRequired()])
    picture_path = FileField(validators=[file_ext_validator(ext=["jpeg", "png", "jpg"])])
    about = TextAreaField("Описание события")
    submit = SubmitField('Отправить')

    def setup_select_field(self, elements):
        self.id_event_type.choices = elements