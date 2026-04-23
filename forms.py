from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Role', choices=[('student', 'Student'), ('faculty', 'Faculty'), ('company', 'Company')], validators=[DataRequired()])
    submit = SubmitField('Register')

class JobForm(FlaskForm):
    title = StringField('Job Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    requirements = TextAreaField('Requirements')
    location = StringField('Location')
    salary_range = StringField('Salary Range')
    application_deadline = StringField('Deadline (YYYY-MM-DD)')
    submit = SubmitField('Post Job')

class StudentProfileForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    student_id_number = StringField('Student ID', validators=[DataRequired()])
    major = StringField('Major', validators=[DataRequired()])
    graduation_year = IntegerField('Graduation Year', validators=[DataRequired()])
    skills = TextAreaField('Skills')
    contact_info = TextAreaField('Contact Info')
    submit = SubmitField('Update Profile')
