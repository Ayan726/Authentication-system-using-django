# Authentication-system-using-django
This Django authentication system allows users to register for an account, log in, log out, and confirm their email address. Upon successful registration, users receive an email with a confirmation link to verify their email address. Once the user has confirmed their email, they can log in to their account and access their dashboard. This project uses Django's built-in authentication system and Django-allauth to implement email confirmation.

# Features
- User registration with email confirmation
- User login and logout
- User dashboard

# Requirements
- Python 3.x
- Django 2.x
- Django-allauth

# Installation
- Clone the repository: git clone https://github.com/Ayan726/Authentication-system-using-django.git
- Create a virtual environment: python3 -m venv env
- Activate the virtual environment: source env/bin/activate
- Install the requirements: pip install -r requirements.txt
- Run migrations: python manage.py migrate
- Run the development server: python manage.py runserver

# Customization
This project can be customized by modifying the templates, forms, and views in the respective directories.

# Contributions
Contributions to this project are welcome. Please open a pull request if you would like to contribute.
