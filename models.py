from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'student', 'faculty', 'company'

    # Relationships
    student = db.relationship('Student', backref='user', uselist=False)
    faculty = db.relationship('Faculty', backref='user', uselist=False)
    company = db.relationship('Company', backref='user', uselist=False)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    student_id_number = db.Column(db.String(20), unique=True, nullable=False)
    major = db.Column(db.String(100), nullable=False)
    graduation_year = db.Column(db.Integer, nullable=False)
    cv_path = db.Column(db.String(200), nullable=True)
    skills = db.Column(db.Text, nullable=True)
    contact_info = db.Column(db.Text, nullable=True)

    # Relationships
    applications = db.relationship('Application', backref='student', lazy=True)

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.Text, nullable=True)

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    website = db.Column(db.String(200), nullable=True)
    contact_person = db.Column(db.String(100), nullable=True)
    contact_email = db.Column(db.String(120), nullable=True)

    # Relationships
    jobs = db.relationship('JobOpportunity', backref='company', lazy=True)

class JobOpportunity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(100), nullable=True)
    salary_range = db.Column(db.String(100), nullable=True)
    application_deadline = db.Column(db.String(20), nullable=True)
    posted_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # Relationships
    applications = db.relationship('Application', backref='job', lazy=True)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('job_opportunity.id'), nullable=False)
    application_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False, default='Applied') # 'Applied', 'Reviewed', 'Interviewed', 'Rejected', 'Hired'
