# Budget Tracker

A Django project for a personal budget tracker. The current site provides public
home, about, features, and contact pages, along with account registration and
login. The `BudgetTracker` app also defines an expense data model associated
with Django users.

## Requirements

- Python 3.12 or newer
- pip

## Setup

From the repository root, create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux, activate it with:

```sh
source .venv/bin/activate
```

Install dependencies, apply database migrations, and start the development
server:

```sh
python -m pip install -r requirements.txt
python WEBSITE/manage.py migrate
python WEBSITE/manage.py runserver
```

Open <http://127.0.0.1:8000/> in a browser. Registration is available at
`/register/`, login at `/login/`, and the Django admin at `/admin/`.

## Tests

Run the Django test suite from the repository root:

```sh
python WEBSITE/manage.py test BudgetTracker
```

## Project layout

```text
WEBSITE/
  BudgetTracker/    App views, routes, models, and tests
  WEBSITE/          Django project settings and root routes
  static/           Project CSS and images
  templates/        HTML templates
  manage.py         Django management entry point
```

The development server uses SQLite by default and stores its local database at
`WEBSITE/db.sqlite3`. That database is intentionally excluded from version
control; create or update it with the migration command above. Gunicorn,
PostgreSQL's `psycopg2` adapter, and WhiteNoise are listed as deployment
dependencies; configure the Django project for the desired production setup
before using them.
