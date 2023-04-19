from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class SearchingForm(FlaskForm):
    searching_label = StringField("Искать здесь...", validators=[DataRequired()])
    submit = SubmitField('Поиск')
