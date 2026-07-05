# 💼 Placement Cell Web Application

> A full-stack web application built using **Python (Flask)** to
> streamline campus recruitment by providing a centralized platform for
> placement administrators and students.

## 📌 Table of Contents

-   Project Overview
-   Objective
-   Problem Statement
-   Solution Approach
-   Key Features
-   System Workflow
-   System Architecture
-   Database Schema
-   Technology Stack
-   Project Structure
-   Future Scope
-   Learning Outcomes
-   Screenshots

------------------------------------------------------------------------

## 📖 Project Overview

The Placement Cell Web Application is a web-based recruitment management
system designed for educational institutions to simplify campus
placement activities.

The platform allows placement administrators to manage job postings
while enabling students to register, browse available opportunities,
upload resumes, and apply for jobs through a centralized portal.

Unlike traditional manual placement processes, this application stores
placement-related information digitally using a relational database,
reducing paperwork and improving accessibility.

> **Current Version:** Job postings are managed by the Placement
> Administrator on behalf of recruiting companies. Company login
> functionality can be integrated in future versions.

------------------------------------------------------------------------

## 🎯 Objective

The primary objective of this project is to digitize the campus
placement process by providing a centralized platform where placement
administrators can efficiently manage job opportunities while students
can register, upload resumes, browse jobs, and apply online.

The application minimizes manual record keeping, improves accessibility,
and organizes placement-related data in a structured database.

------------------------------------------------------------------------

## ❗ Problem Statement

Many educational institutions still rely on manual placement processes
involving spreadsheets, emails, and paper-based records.

Challenges include:

-   Manual job posting
-   Manual student registration
-   Resume collection through emails
-   Difficulty managing job applications
-   Lack of a centralized placement portal
-   Scattered placement preparation resources

------------------------------------------------------------------------

## 💡 Solution Approach

The application provides a centralized digital portal where placement
administrators can publish job opportunities and students can:

-   Register for placements
-   Upload resumes
-   Browse available jobs
-   Apply online
-   Access placement preparation resources

All information is stored using SQLite through SQLAlchemy ORM.

------------------------------------------------------------------------

## ✨ Key Features

### 👨‍💼 Placement Administrator

-   Post new job opportunities
-   Publish company recruitment details
-   Manage job listings
-   Store job details in the database
-   Success notification after posting jobs

### 🎓 Student Module

-   Student Registration
-   Browse Available Jobs
-   Online Job Application
-   Resume Upload
-   PDF Resume Validation (Max 5 MB)
-   Duplicate Application Prevention
-   Success notification after application submission

### 📚 Placement Resources

-   Resume Building Tips (External Link)
-   Interview Preparation (External Link)
-   Placement Guidance Resources

### 🗄️ Database Management

The backend manages three tables:

-   **JobPost**
-   **Registration**
-   **JobApplicantDetails**

------------------------------------------------------------------------

## ⚙️ System Workflow

### Step 1 -- Job Posting

Placement Administrator opens the **Post Job** page.

The administrator enters:

-   Job Title
-   Company Name
-   Location
-   Salary
-   Description
-   Requirements

↓

Job information is stored inside the **JobPost** table.

↓

A confirmation popup notifies that the job has been posted successfully.

------------------------------------------------------------------------

### Step 2 -- Student Registration

Students register by entering:

-   Name
-   Email
-   Phone Number
-   Degree
-   Resume

↓

Resume is uploaded to the **uploads/** directory.

↓

Registration details are stored inside the **Registration** table.

------------------------------------------------------------------------

### Step 3 -- Browse Jobs

Students visit the **Student Resources** page.

↓

Available jobs are fetched dynamically from the database using
SQLAlchemy and displayed using Jinja2 templates.

------------------------------------------------------------------------

### Step 4 -- Apply for Job

Students click **Apply Now**.

The application form collects:

-   First Name
-   Last Name
-   Course
-   Branch
-   Year of Passing
-   Organisation Name
-   Permanent Address
-   Email
-   Contact Number
-   Resume (PDF only)

↓

Application is validated.

↓

Duplicate applications are prevented using Email + Job ID validation.

↓

Application data is stored inside the **JobApplicantDetails** table.

↓

A success popup confirms successful submission.

------------------------------------------------------------------------

## 🏗️ System Architecture

``` mermaid
flowchart TD
A[Placement Administrator] --> B[Flask Application]
C[Student] --> B
B --> D[Job Management]
B --> E[Student Registration]
B --> F[Job Application]
D --> G[(SQLite Database)]
E --> G
F --> G
F --> H[uploads/]
G --> I[JobPost]
G --> J[Registration]
G --> K[JobApplicantDetails]
```

------------------------------------------------------------------------

## 🗄️ Database Schema

### JobPost

  Column
  --------------
  id
  title
  company
  location
  description
  requirements
  salary

### Registration

  Column
  -----------------
  id
  name
  email
  phone
  degree
  resume_filename

### JobApplicantDetails

  Column
  -------------------
  id
  job_id
  first_name
  last_name
  course
  branch
  yop
  organisation_name
  permanent_address
  email
  contact
  resume_filename

------------------------------------------------------------------------

## 🛠️ Technology Stack

  Technology   Purpose
  ------------ ---------------------
  Python       Backend Programming
  Flask        Web Framework
  SQLAlchemy   ORM
  SQLite       Database
  HTML5        Page Structure
  CSS3         Styling
  Bootstrap    Responsive UI
  Jinja2       Dynamic Templates
  Werkzeug     Secure File Upload

------------------------------------------------------------------------

## 📂 Project Structure

``` text
PLACEMENTWEBPAGE/
├── app.py
├── instance/
│   └── jobs.db
├── uploads/
├── static/
├── templates/
└── README.md
```

------------------------------------------------------------------------

## 🚀 Future Scope

-   Company login and authentication
-   Student login and profile management
-   Placement Officer dashboard
-   Resume shortlisting
-   Application status tracking
-   Email notifications
-   Interview scheduling
-   Search and filter jobs
-   Analytics dashboard
-   Role-based authentication
-   Cloud database integration

------------------------------------------------------------------------

## 🎓 Learning Outcomes

-   Flask Web Development
-   SQLAlchemy ORM
-   SQLite Database
-   CRUD Operations
-   File Upload Handling
-   Form Validation
-   Jinja2 Templates
-   Responsive UI Design
-   Database Relationships
-   Dynamic Routing

------------------------------------------------------------------------

## 📸 Screenshots

Include screenshots of:

-   Home Page
-   Student Registration
-   Job Posting
-   Job Listings
-   Job Application Form
-   Contact Page
-   Student Resources

------------------------------------------------------------------------

## 👨‍💻 Author

**Prashant Kumar Baranwal**

B.Tech Computer Science & Engineering
