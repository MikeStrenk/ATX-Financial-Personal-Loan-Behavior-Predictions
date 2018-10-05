from flask_wtf import FlaskForm
from wtforms import TextField, SelectField, IntegerField, Form, BooleanField, StringField, PasswordField, validators, SubmitField
from wtforms.validators import DataRequired, AnyOf, NoneOf


class ApplicationForm(FlaskForm):
    firstname = StringField("First Name: ", validators=[DataRequired()])
    lastname = StringField("Last Name: ", validators=[DataRequired()])
    grade = SelectField("Credit Score: ", choices=[
        ('Choose', 'Choose'),
        ('>750', '>750'),
        ('>700', '>700'),
        ('>650', '>650'),
        ('>625', '>625'),
        ('>600', '>600'),
        ('>550', '>550'),
        ("Bad Credit", "Bad Credit")],
        validators=[AnyOf(['>750', '>700', '>650', '>650', '>600', '>550', "Bad Credit"])])
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
    Housing_MORTGAGE = SelectField(
        "Mortgage?: ", choices=[('Choose', 'Choose'), ('Yes', 'Yes'), ('No', 'No')], validators=[AnyOf(['Yes', 'No'])])
    Housing_OWN = SelectField("Own your Home?: ", choices=[(
        'Choose', 'Choose'), ('Yes', 'Yes'), ('No', 'No')], validators=[AnyOf(['Yes', 'No'])])
    Housing_RENT = SelectField("Rent your Home?: ", choices=[(
        'Choose', 'Choose'), ('Yes', 'Yes'), ('No', 'No')], validators=[AnyOf(['Yes', 'No'])])
