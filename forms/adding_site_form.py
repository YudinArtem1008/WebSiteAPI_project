from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired


class AddingSiteForm(FlaskForm):
    url = StringField("Введите url сайта", validators=[DataRequired()])
    hypertext = StringField("Введите название сайта", validators=[DataRequired()])
    about = TextAreaField("Расскажите немного о сайте", validators=[DataRequired()])
    submit = SubmitField('Поиск')
