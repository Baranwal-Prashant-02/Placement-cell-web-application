💼 Placement Cell Web Application

A full-stack web application built using Python (Flask) to streamline campus recruitment by providing a centralized platform for placement administrators and students. The system enables administrators to publish job opportunities while allowing students to register, explore openings, upload resumes, and submit online job applications.

📌 Table of Contents
Project Overview
Objective
Problem Statement
Solution Approach
Features
System Workflow
System Architecture
Database Design
Technology Stack
Project Structure
Installation
Future Scope
Learning Outcomes


📖 Project Overview

The Placement Cell Web Application is a web-based recruitment management system designed for educational institutions to simplify campus placement activities.

The platform allows placement administrators to manage job postings while enabling students to register, browse available opportunities, upload resumes, and apply for jobs through a centralized portal.

Unlike traditional manual placement processes, this application stores all placement-related information digitally using a relational database, reducing paperwork and improving accessibility.

Current Version: Job postings are managed by the Placement Administrator on behalf of recruiting companies. Company login functionality can be integrated in future versions.

🎯 Objective

The primary objective of this project is to digitize the campus placement process by providing a centralized platform where placement administrators can efficiently manage job opportunities and students can easily register, upload resumes, and apply for jobs online.

The application minimizes manual record keeping, improves accessibility, and organizes placement-related data in a structured database for efficient management.

❗ Problem Statement

Many educational institutions still rely on manual placement processes involving spreadsheets, emails, and physical documents.

This creates several challenges:

Manual job posting and student registration
Resume collection through emails
Difficulty managing multiple job applications
Lack of centralized placement information
Inefficient record management
Limited access to placement preparation resources
💡 Solution Approach

The Placement Cell Web Application provides a centralized digital platform that connects placement administrators and students.

The application enables administrators to publish job opportunities while allowing students to:

Register for placement activities
Upload resumes
Browse available job openings
Apply online using structured application forms
Access placement preparation resources

All information is securely stored in an SQLite database through SQLAlchemy ORM, ensuring efficient retrieval and management.

✨ Key Features
👨‍💼 Placement Administrator
Post new job opportunities
Manage available job listings
Publish company recruitment details
Store job information in database
Success notification after posting jobs
🎓 Student Module
Student Registration
Resume Upload
Browse Available Jobs
Online Job Application
Mandatory Application Form
Duplicate Application Prevention
PDF Resume Validation (Maximum 5 MB)
Application Success Notification
📚 Placement Resources

The application also provides quick access to external learning resources including:

Resume Building Tips
Interview Preparation
Placement Guidance

These hyperlinks redirect students to trusted external websites for career preparation.

🗂 Database Management

The backend manages three relational tables:

1. JobPost

Stores company recruitment information:

Job Title
Company Name
Location
Description
Requirements
Salary
2. Registration

Stores registered student details:

Name
Email
Phone Number
Degree
Uploaded Resume Filename
3. JobApplicantDetails

Stores detailed job application records:

Job ID (Foreign Key)
First Name
Last Name
Course
Branch
Year of Passing
Organisation Name
Permanent Address
Email
Contact Number
Uploaded Resume Filename

Each application is linked to a specific job using the Job ID, enabling organized storage of applicant information.

⚙️ System Workflow
Step 1 — Job Posting

Placement Administrator opens the Post Job page.

The following details are entered:

Job Title
Company Name
Location
Salary
Description
Requirements

↓

Job information is stored inside the JobPost table.

↓

A confirmation popup notifies that the job has been posted successfully.

Step 2 — Student Registration

Students register by entering:

Name
Email
Phone Number
Degree
Resume

↓

Resume is uploaded to the uploads/ directory.

↓

Registration details are stored inside the Registration table.

Step 3 — Browse Jobs

Students visit the Student Resources page.

↓

Available jobs are dynamically fetched from the SQLite database using SQLAlchemy.

↓

Job cards are rendered using Jinja2 templates.

Step 4 — Apply for Job

When students click Apply Now

↓

Application form opens.

↓

Student provides:

First Name
Last Name
Course
Branch
Year of Passing
Organisation Name
Permanent Address
Email
Contact Number
Resume (PDF)

↓

Application is validated.

↓

Duplicate applications for the same job are prevented using Email + Job ID validation.

↓

Application details are stored inside the JobApplicantDetails table.

↓

Student receives:

Application Submitted Successfully
🏗 System Architecture
                    Placement Administrator
                              │
                              │
                       Post Job Details
                              │
                              ▼
                     Flask Application
                  (Python Backend Server)
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
   Job Management      Student Registration   Job Application
        │                     │                     │
        └──────────────┬──────┴──────────────┬──────┘
                       ▼                     ▼
                SQLAlchemy ORM
                       │
                       ▼
              SQLite Database (jobs.db)
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
  Job Records                 Student & Application Records
                       │
                       ▼
               Resume Storage (uploads/)
🗄 Database Schema
JobPost
│
├── id
├── title
├── company
├── location
├── description
├── requirements
└── salary
Registration
│
├── id
├── name
├── email
├── phone
├── degree
└── resume_filename
JobApplicantDetails
│
├── id
├── job_id (Foreign Key)
├── first_name
├── last_name
├── course
├── branch
├── yop
├── organisation_name
├── permanent_address
├── email
├── contact
└── resume_filename
🛠 Technology Stack
Technology	Why it is Used
Python	Core programming language used for backend development
Flask	Handles routing, request processing, server-side rendering, and application logic
SQLAlchemy	ORM used to interact with the database using Python models instead of raw SQL queries
SQLite	Lightweight relational database used to store job postings, student registrations, and job applications
HTML5	Structures web pages and application forms
CSS3	Styles the user interface and improves visual presentation
Bootstrap	Provides responsive layouts, cards, buttons, forms, and grid system
Jinja2	Dynamically renders database content into HTML templates
Werkzeug	Secures uploaded filenames and manages resume file uploads
📂 Project Structure
PLACEMENTWEBPAGE/
│
├── app.py                     # Main Flask application
├── instance/
│   └── jobs.db                # SQLite database
│
├── uploads/                   # Uploaded PDF resumes
│
├── static/
│   ├── about.css
│   ├── companies.css
│   ├── contact.css
│   ├── login.css
│   ├── registration.css
│   ├── std-resources.css
│   ├── styles.css
│   └── ...
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── login.html
│   ├── registration.html
│   ├── post_job.html
│   ├── student-resources.html
│   ├── apply_job.html
│   ├── placement.html
│   └── ...
│
└── README.md
🚀 Future Scope
Company login and authentication
Student authentication and profile management
Placement Officer Dashboard
Application status tracking (Applied, Shortlisted, Selected, Rejected)
Email notifications
Interview scheduling
Resume shortlisting
Search and filter jobs
Analytics dashboard
Password reset functionality
Role-based authentication
MySQL/PostgreSQL integration
Cloud deployment (Render, Railway, AWS)
🎓 Learning Outcomes

This project helped me gain practical experience in:

Flask Web Development
SQLAlchemy ORM
SQLite Database Design
CRUD Operations
File Upload Handling
Form Validation
Server-side Rendering with Jinja2
Responsive UI Design using Bootstrap
Database Relationships
Dynamic Routing
MVC-inspired Project Structure
Web Application Development
📸 Screenshots

Include screenshots of:

🏠 Home Page
📝 Student Registration
💼 Post Job Page
📋 Job Listings
📄 Job Application Form
📚 Student Resources
📞 Contact Page
⭐ Highlights
Full-stack Flask web application
Database-driven dynamic job portal
Resume upload with secure file handling
Online job application workflow
Duplicate application prevention
Responsive Bootstrap interface
Modular project structure using Flask, SQLAlchemy, and Jinja2
Clean separation of frontend, backend, and database layers
