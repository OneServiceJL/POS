# Django CV & Portfolio Sample Website

This repository contains a Django sample website for managing a professional CV and portfolio.

## Features
- Resume / profile presentation
- Skills, experience, and education sections
- Portfolio project listing and detail pages
- Contact form backed by Django models
- Admin interface for full content management

## Setup
1. Install dependencies:
   ```bash
   python3 -m pip install -r requirements.txt
   ```
2. Apply database migrations:
   ```bash
   python3 manage.py migrate
   ```
3. Create a superuser to manage content:
   ```bash
   python3 manage.py createsuperuser
   ```
4. Run the development server:
   ```bash
   python3 manage.py runserver
   ```
5. Visit the site:
   - Home: `http://127.0.0.1:8000/`
   - Admin: `http://127.0.0.1:8000/admin/`

## Admin Models
- Profile
- Skill
- Experience
- Education
- Project
- Contact Messages

## Notes
Add your resume and portfolio items through the admin interface for a complete live site experience.
