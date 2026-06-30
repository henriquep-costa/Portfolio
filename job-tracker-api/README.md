Job Tracker – Django Backend Project
 - Overview

Job Tracker is a backend web application built with Django to manage job applications.

The system allows users to:

Register companies

Track job applications

Define application status (Applied, Interview, Rejected, Offer)

Prevent duplicate applications for the same position

This project was built to practice backend development concepts such as relational modeling, database constraints, and Django ORM.

 - Main Concepts Applied

Relational database modeling

ForeignKey relationships (1-N)

One-to-one relationships

Unique database constraints

Django ORM

Data integrity rules

 - Database Structure

The system contains three main models:

User (Django built-in model)

Company

Application

Application connects User and Company and prevents duplicate entries using a UniqueConstraint.

 - Technologies Used

Python

Django

SQLite (default)

Git & GitHub

 -  How to Run Locally

Clone the repository:

git clone <repository-url>

Create virtual environment:

python -m venv venv

Activate virtual environment:

Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Apply migrations:

python manage.py migrate

Run server:

python manage.py runserver
 -  Possible Improvements

Authentication system with login/logout

REST API using Django REST Framework

Deployment to cloud platform

Frontend integration

Dashboard with analytics


Henrique Costa
Backend Developer in Training
