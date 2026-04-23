import os
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Student, Faculty, Company, JobOpportunity, Application
from forms import LoginForm, RegistrationForm, JobForm, StudentProfileForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campus.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password_hash=hashed_pw, role=form.role.data)
        db.session.add(new_user)
        db.session.commit()
        
        # Create profile based on role
        if form.role.data == 'student':
            profile = Student(user_id=new_user.id, name=new_user.username, student_id_number='', major='', graduation_year=2024)
        elif form.role.data == 'faculty':
            profile = Faculty(user_id=new_user.id, name=new_user.username, department='')
        else:
            profile = Company(user_id=new_user.id, name=new_user.username)
        
        db.session.add(profile)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'student':
        jobs = JobOpportunity.query.all()
        # Find jobs the student has applied for
        applied_job_ids = [app.job_id for app in Application.query.filter_by(student_id=current_user.student.id).all()]
        return render_template('student_dashboard.html', jobs=jobs, applied_job_ids=applied_job_ids)
    elif current_user.role == 'faculty':
        students = Student.query.all()
        jobs = JobOpportunity.query.all()
        return render_template('faculty_dashboard.html', students=students, jobs=jobs)
    elif current_user.role == 'company':
        jobs = JobOpportunity.query.filter_by(company_id=current_user.company.id).all()
        return render_template('company_dashboard.html', jobs=jobs)
    return redirect(url_for('index'))

@app.route('/post_job', methods=['GET', 'POST'])
@login_required
def post_job():
    if current_user.role != 'company':
        return redirect(url_for('dashboard'))
    form = JobForm()
    if form.validate_on_submit():
        job = JobOpportunity(
            company_id=current_user.company.id,
            title=form.title.data,
            description=form.description.data,
            requirements=form.requirements.data,
            location=form.location.data,
            salary_range=form.salary_range.data,
            application_deadline=form.application_deadline.data
        )
        db.session.add(job)
        db.session.commit()
        flash('Job posted successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('post_job.html', form=form)

@app.route('/apply/<int:job_id>')
@login_required
def apply(job_id):
    if current_user.role != 'student':
        return redirect(url_for('dashboard'))
    existing_app = Application.query.filter_by(student_id=current_user.student.id, job_id=job_id).first()
    if existing_app:
        flash('You have already applied for this job.', 'info')
    else:
        app_entry = Application(student_id=current_user.student.id, job_id=job_id)
        db.session.add(app_entry)
        db.session.commit()
        flash('Application submitted successfully!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if current_user.role == 'student':
        form = StudentProfileForm(obj=current_user.student)
        if form.validate_on_submit():
            form.populate_obj(current_user.student)
            db.session.commit()
            flash('Profile updated!', 'success')
            return redirect(url_for('dashboard'))
        return render_template('profile.html', form=form)
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
