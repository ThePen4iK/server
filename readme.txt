1. make virtual environment
    python -m venv venv

2. activate it:
    venv\scripts\activate

3. install requirements:
    venv\scripts\activate

4. apply migrations:
    python manage.py migrate

5. make .env file as .env.example and provide secret key (random string)

6. run server
    python manage.py runserver

7. Swagger available at:
    127.0.0.1:8000/swagger