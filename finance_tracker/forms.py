from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, IntegerField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from finance_tracker.models import User
from flask_login import current_user

class regForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=4, max=24)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class loginForm(FlaskForm):
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=4, max=24)])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign In")

class updateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators = [FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Update")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')
            
class EntryForm(FlaskForm):
    amount = IntegerField('Amount', validators=[DataRequired()])
    type = RadioField('Type', choices=[('income', 'Income'), ('expense', 'Expense')], validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('food', 'Food & Dining'), 
        ('transport', 'Transport'), 
        ('shopping', 'Shopping'), 
        ('entertainment', 'Entertainment'), 
        ('monthly', 'Monthly'), 
        ('deposit', 'Deposit'), 
        ('investment', 'Investment')],
        validators=[DataRequired()])
    note = StringField('Note', validators=[Length(max=20)])
    submit = SubmitField('Add Entry')
