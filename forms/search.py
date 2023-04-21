from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, BooleanField
from wtforms.validators import Optional


class SearchingForm(FlaskForm):
    searching_label = StringField("Искать здесь...", validators=[Optional()])
    speech_moving = BooleanField("Перейти в поиск по голосу?")
    speak = SubmitField('Говорить')
    submit = SubmitField('Поиск')
