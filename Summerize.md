# Project Summary: Auth_Service

## Overview

This project is a Django-based authentication service designed for a multi-tenant SaaS (Software as a Service) application, likely targeting the BTP (Bâtiment et Travaux Publics - Construction and Public Works) industry. It provides a robust and secure way to manage users, their roles, and their access to the system based on their company (tenant).

## Key Features

*   **Multi-tenancy:** The system is designed to support multiple client companies (tenants) in an isolated manner. Each user is associated with a `tenant_id`, ensuring that data and access are segregated between different companies.
*   **Role-Based Access Control (RBAC):** The `CustomUser` model includes a `role` field that defines the user's permissions within the application. The roles are specific to the BTP industry, including 'Directeur' (Director), 'Conducteur de Travaux' (Works Manager), 'Ressources Humaines' (Human Resources), 'Employé de Chantier' (Site Employee), and 'Administrateur SaaS' (SaaS Administrator).
*   **JWT Authentication:** The service uses JSON Web Tokens (JWT) for authentication, which is a standard for creating access tokens for an application. The `rest_framework_simplejwt` library is used for this purpose.
*   **API Endpoints:** The service exposes several API endpoints for user management:
    *   `POST /api/auth/register/`: Allows new users to register.
    *   `GET /api/auth/protected-test/`: A protected endpoint to test if a user is properly authenticated with a valid JWT.
    *   `POST /api/auth/request-reset-email/`: Initiates the password reset process by sending an email to the user.
    *   `POST /api/auth/password-reset-confirm/<uidb64>/<token>/`: Allows a user to set a new password using the token received in the reset email.
    *   `POST /api/token/`: Obtains a JWT token pair (access and refresh).
    *   `POST /api/token/refresh/`: Refreshes an expired access token.
*   **Web Interface for API Testing:**
    *   The project now includes a simple web interface to facilitate testing the APIs.
    *   The interface provides forms for registration, login, requesting password resets, and testing protected endpoints.
    *   These pages are available under the `/auth/` path (e.g., `/auth/login/`, `/auth/register/`).
    *   The root of the application redirects to the login page.
*   **Custom User Model:** The project uses a custom user model (`core_auth.CustomUser`) that extends Django's `AbstractUser`. This model uses the email address as the unique identifier for login (`USERNAME_FIELD = 'email'`).
*   **Email Integration:** The service is configured to send password reset emails using a Gmail SMTP server. It uses a custom HTML template (`password_reset.html`) for the email content. The password reset link in the email is dynamically generated to point to the web interface.

## Technical Stack

*   **Backend Framework:** Django
*   **API:** Django Rest Framework
*   **Authentication:** `rest_framework_simplejwt` (JSON Web Tokens)
*   **Database:** SQLite (for development)
*   **Dependencies:**
    *   `django`
    *   `djangorestframework`
    *   `djangorestframework-simplejwt`
    *   `python-dotenv`

## Project Structure

*   **`Auth_Service/`**: The main Django project directory.
    *   `settings.py`: Contains the project settings, including database configuration, installed apps, and JWT settings.
    *   `urls.py`: The root URL configuration for the project.
*   **`core_auth/`**: The core application for handling authentication.
    *   `models.py`: Defines the `CustomUser` model with `tenant_id` and `role` fields.
    *   `views.py`: Contains the logic for the API endpoints (registration, password reset, etc.).
    *   `template_views.py`: Contains the logic for rendering the HTML templates for API testing.
    *   `serializers.py`: Defines the serializers for the `CustomUser` model and for handling password reset requests.
    *   `urls.py`: The URL configuration for the `core_auth` app's API endpoints.
    *   `templates_urls.py`: The URL configuration for the web interface pages.
*   **`templates/`**: Contains the HTML templates.
    *   `email/`: Contains the email templates.
    *   `core_auth/`: Contains the templates for the web interface.
*   **`manage.py`**: The command-line utility for Django.
*   **`README.md`**: Provides instructions on how to set up and run the project.
