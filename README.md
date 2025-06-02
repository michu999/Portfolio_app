# Portfolio App

A Django-based portfolio web application for users to showcase their projects, update their profiles, and interact with others.

## Features

- **User Authentication:** Register, log in, and manage your account securely.
- **Profile Management:**
  - Upload, update, or remove your profile picture.
  - Edit your email, bio, and LinkedIn URL.
  - Fallback avatar with user initial if no profile picture is set.
- **Project Showcase:**
- **Comments:** Users can comment on projects, with each comment showing the author's profile picture or fallback avatar.
- **Responsive Design:** Styled with Tailwind CSS for a modern, mobile-friendly interface.

## Tech Stack

- **Backend:** Django 5.2.1
- **Frontend:** Tailwind CSS, HTML
- **Database:** PostgreSQL
- **Other:** django-crispy-forms, django-tailwind, allauth

## Setup

1. Clone the repository.
2. Install dependencies:
pip install -r requirements.txt npm install
4. Start the development server:
python manage.py runserver
5. Access the app at `http://localhost:8000/`.

## Customization

- Update profile picture and details from the profile page.
- Add or edit projects from your dashboard.
- Comment on projects to interact with other users.

## License

This project is for educational purposes.
