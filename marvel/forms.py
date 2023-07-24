import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField, DateTimeField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    email = StringField('email', validators= [DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit_button = SubmitField()

class MarvelForm(FlaskForm):

    name = StringField('name')
    description = StringField('description')
    comics_appeared_in = DecimalField('comics_appeared_in', places=1)
    super_power = StringField('super_power')
    date_created = StringField('date_created')
    submit_button = SubmitField()
