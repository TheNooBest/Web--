from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class NewThreadForm(FlaskForm):
    title = StringField('Название треда: ', validators=[DataRequired()])
    message = TextAreaField('Сообщение: ', validators=[DataRequired()])
