# Django_Project

A Django-based website project (WEBSITE folder) for sehiyojo-maker.

Languages: HTML, Python, CSS.

## Project structure (partial)

- WEBSITE/ - Django project and app content (templates, static, views)

## Quickstart (development)

1. Clone the repository:

   git clone https://github.com/sehiyojo-maker/Django_Project.git
   cd Django_Project

2. Create and activate a virtual environment (recommended):

   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate    # Windows (PowerShell)

3. Install dependencies:

   pip install -r requirements.txt

4. Configure environment variables (SECRET_KEY, DATABASE settings) as needed.

5. Apply migrations and run the development server:

   python manage.py migrate
   python manage.py runserver

6. Open http://127.0.0.1:8000/ in your browser.

## Notes

- The `WEBSITE/` directory contains templates and static HTML (most of the repo is HTML/CSS).
- For production, configure a proper database, static file serving, and a WSGI/ASGI server (e.g., Gunicorn + Nginx).

