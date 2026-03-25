from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, IntegerField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

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
