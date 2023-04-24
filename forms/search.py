from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, BooleanField
from wtforms.validators import Optional


class SearchingForm(FlaskForm):
    searching_label = StringField("Искать здесь...", validators=[Optional()])
    submit = SubmitField('Поиск')
