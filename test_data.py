from app import app, db
from models import User, Student, Faculty, Company, JobOpportunity
from werkzeug.security import generate_password_hash

def create_test_data():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create Users
        hashed_pw = generate_password_hash('password123')
        
        # 1. Student
        u1 = User(username='student1', email='student1@example.com', password_hash=hashed_pw, role='student')
        db.session.add(u1)
        db.session.commit()
        s1 = Student(user_id=u1.id, name='Ahmed Ali', student_id_number='CS101', major='Computer Science', graduation_year=2024, skills='Python, Flask, SQL')
        db.session.add(s1)

        # 2. Faculty
        u2 = User(username='faculty1', email='faculty1@example.com', password_hash=hashed_pw, role='faculty')
        db.session.add(u2)
        db.session.commit()
        f1 = Faculty(user_id=u2.id, name='Dr. Sarah Smith', department='Information Technology')
        db.session.add(f1)

        # 3. Company
        u3 = User(username='techcorp', email='hr@techcorp.com', password_hash=hashed_pw, role='company')
        db.session.add(u3)
        db.session.commit()
        c1 = Company(user_id=u3.id, name='TechCorp Solutions', description='A leading software company.')
        db.session.add(c1)
        db.session.commit()

        # Create Job Opportunities
        j1 = JobOpportunity(company_id=c1.id, title='Software Engineer Intern', description='Join our team as an intern.', location='Remote', salary_range='500-1000 USD', application_deadline='2024-12-31')
        j2 = JobOpportunity(company_id=c1.id, title='Data Analyst', description='Analyze complex data sets.', location='New York', salary_range='3000-5000 USD', application_deadline='2024-11-30')
        db.session.add(j1)
        db.session.add(j2)
        
        db.session.commit()
        print("Test data created successfully!")

if __name__ == '__main__':
    create_test_data()
