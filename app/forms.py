from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class FormZero(FlaskForm):
    name = StringField('Name')
    age = StringField('Age')
    country = StringField('Country')
    occupation = StringField('Occupation')
    submit = SubmitField('Next')

class FormOne(FlaskForm):
    myers = StringField('Myers')
    interests = StringField('Interests')
    sports = StringField('Sports')
    songs = StringField('Songs')
    languages = StringField('Languages')
    food = StringField('Food')
    otherActivities = StringField('OtherActivities')
    submit = SubmitField('Next')

class FormTwo(FlaskForm):
    gender = StringField('Gender')
    ethnicity = StringField('Ethnicity')
    socialClass = StringField('Socialclass')
    university = StringField('University')
    submit = SubmitField('Finish')