# CampusConnect - Campus Automation System

## Overview

CampusConnect is a web-based Campus Automation System designed to streamline the placement process for college students, faculty, and visiting companies. Built with Python and Flask, this system provides dedicated portals for each user role, facilitating job postings, student applications, and profile management.

## Features

### For Students:
*   **Profile Management:** Create and update personal profiles, including academic details, skills, and contact information.
*   **Job Application:** Browse available job opportunities and apply with a single click.
*   **Application Tracking:** View the status of submitted job applications.

### For Faculty:
*   **Student Overview:** Access a list of registered students and their profiles.
*   **Job Monitoring:** View all active job postings from companies.
*   **Placement Management:** (Future enhancement) Tools for managing placement drives and student-company interactions.

### For Companies:
*   **Company Profile:** Manage company details and contact information.
*   **Job Posting:** Create and publish new job opportunities for students.
*   **Applicant Review:** (Future enhancement) View and manage applications received for posted jobs.

## Technology Stack

*   **Backend:** Python, Flask
*   **Database:** SQLite (for development), SQLAlchemy ORM
*   **Authentication:** Flask-Login
*   **Forms:** Flask-WTF
*   **Frontend:** HTML, CSS (Bootstrap 5)

## Setup and Installation

To get the CampusConnect system up and running on your local machine, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/campus_automation.git
cd campus_automation
```

### 2. Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the Database and Create Test Data

```bash
python3 test_data.py
```

### 5. Run the Application

```bash
python3 app.py
```

The application will be accessible at `http://127.0.0.1:5000`.

## Usage

1.  **Register:** Create accounts for different roles (student, faculty, company).
2.  **Login:** Access your respective dashboard.
3.  **Explore:**
    *   **Students:** Update your profile, browse jobs, and apply.
    *   **Companies:** Post new job opportunities.
    *   **Faculty:** View registered students and active job postings.

## Contributing

Contributions are welcome! Please feel free to fork the repository, create a new branch, and submit a pull request with your enhancements.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries, please contact [Your Name/Email].
