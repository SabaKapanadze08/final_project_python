from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, EmailField, PasswordField, IntegerField, FileField

from wtforms.validators import DataRequired, Length, EqualTo, NumberRange

class RegisterForm (FlaskForm):
    email = EmailField("Email address", validators=[DataRequired(), Length(max=80)])
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=32)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    retypePassword = PasswordField("Retype Password", validators=[DataRequired(), EqualTo('password')])
    role = StringField()
    submit = SubmitField("Sign Up")

class LoginForm (FlaskForm):
    email = EmailField("Email address", validators=[DataRequired(), Length(max=80)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Sign In")

class ContactForm (FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=30)])
    email = EmailField("Email", validators=[DataRequired(), Length(max=80)])
    message = StringField("Message", validators=[DataRequired(), Length(max=400)])
    submit = SubmitField("Send Message")

class ReviewForm(FlaskForm):
    author_name = StringField('Author Name', validators=[DataRequired(), Length(min=2, max=100)])
    author_initials = StringField('Author Initials', validators=[DataRequired(), Length(min=1, max=10)])
    rating = IntegerField('Rating', validators=[DataRequired(), NumberRange(min=1, max=5)])
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit Review')   

class ServiceForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    image = FileField('Image', validators=[DataRequired()])
    submit = SubmitField('Add Service')    
