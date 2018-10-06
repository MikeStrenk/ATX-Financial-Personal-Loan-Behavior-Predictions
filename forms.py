from flask_wtf import FlaskForm
from wtforms import TextField, SelectField, IntegerField, Form, BooleanField, StringField, PasswordField, validators, SubmitField
from wtforms.validators import DataRequired, AnyOf, NoneOf


class DeleteRowForm(FlaskForm):
    ID = IntegerField('Delete Row: ', validators=[DataRequired()])


class ApplicationForm(FlaskForm):
    age = IntegerField("Age: ", validators=[DataRequired()])
    occupation = StringField("Occupation: ", validators=[DataRequired()])
    grade = SelectField("Credit Score: ", choices=[
        ('Choose', 'Choose'),
        ('750', '750'),
        ('700', '700'),
        ('650', '650'),
        ('625', '625'),
        ('600', '600'),
        ('550', '550'),
        ("Bad Credit", "Bad Credit")],
        validators=[AnyOf(['750', '700', '650', '625', '600', '550', "Bad Credit"])])
    Years_At_present_Employment = IntegerField(
        "Years at present employment: ", validators=[DataRequired()])
    expenses = IntegerField(
        "Monthly Expenses: ", validators=[DataRequired()])
    income = IntegerField(
        "Annual Salary: ", validators=[DataRequired()])
    Delinquency = SelectField(
        "Have you ever been delinquent on a loan?: ", choices=[('Choose', 'Choose'), ('Yes', 'Yes'), ('No', 'No')], validators=[AnyOf(['Yes', 'No'])])
    Collections = SelectField(
        "Have you ever been in collections on a loan?: ", choices=[('Choose', 'Choose'), ('Yes', 'Yes'), ('No', 'No')], validators=[AnyOf(['Yes', 'No'])])
    Derogatory = SelectField(
        "Do you have a derogatory item on a loan?: ", choices=[('Choose', 'Choose'), ('Yes', 'Yes'), ('No', 'No')], validators=[AnyOf(['Yes', 'No'])])
    Housing = SelectField(
        "What is your housing situation?: ",
        choices=[('Choose', 'Choose'),
                 ('Own my home', 'Own my home'),
                 ('Mortgage', 'Mortgage'),
                 ('Rent', 'Rent'),
                 ('Live with Parents',
                  'Live with Parents')],
        validators=[AnyOf([
            'Own my home',
            'Mortgage',
            'Rent',
            'Live with Parents'])])
