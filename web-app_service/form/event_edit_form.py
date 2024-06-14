from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FileField, DateTimeLocalField
from wtforms.validators import DataRequired
from form.custom_validators import file_ext_validator


class EventEditForm(FlaskForm):
    event_name = StringField('Название события', validators=[DataRequired()])
    date_of_start = DateTimeLocalField('Дата начала', format="%Y-%m-%dT%H:%M", validators=[DataRequired()])
    address = StringField('Местоположение', validators=[DataRequired()])
    picture_path = FileField(validators=[file_ext_validator(ext=["jpeg", "png", "jpg"])])
    about = TextAreaField("Описание события")
    submit = SubmitField('Отправить')

    def format_date(self, date):
        part_of_date = "-".join(date.split()[0].split('.')[::-1])
        date_of_start = "T".join([part_of_date, date.split()[1]])
        date_of_start = datetime.fromisoformat(date_of_start)
        return date_of_start

    def autofill(self, event):
        self.event_name.data = event["event_name"]
        self.date_of_start.data = self.format_date(event["date_of_start"])
        self.address.data = event["address"]
        self.about.data = event["about"]
