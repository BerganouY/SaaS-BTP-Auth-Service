# Auth_Service

A Django authentication service.

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* Python 3.10
* Pip
* Virtualenv

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/BerganouY/SaaS-BTP-Auth-Service.git
   ```
2. Create a virtual environment
   ```sh
   virtualenv .venv
   ```
3. Activate the virtual environment
   ```sh
   source .venv/bin/activate
   ```
4. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
5. Run migrations
   ```sh
   python manage.py migrate
   ```
6. Start the server
   ```sh
   python manage.py runserver
   ```

## Web Interface

This project includes a simple web interface to test the API. Once you start the server, you can access it at `http://127.0.0.1:8000/`.

The following pages are available:
*   `/auth/login/`: Login page to obtain a JWT token.
*   `/auth/register/`: Registration page for new users.
*   `/auth/request-password-reset/`: Page to request a password reset email.
*   `/auth/protected-test/`: A page to test access to a protected resource using a JWT.

## Running the tests

To run the tests, run the following command:

```sh
python manage.py test
```