# Django-Hearthlight
A Django port of the Hearthlight website.

## Getting Started

This repository lives inside a meta directory that also holds the Docker Compose files used to run the PostgreSQL database.

### 1. Create the meta directory and clone the repo

```bash
mkdir Django-Hearthlight
cd Django-Hearthlight
git clone <repo-url> Hearthlight
```

### 2. Add Docker files

Obtain `docker-compose.yaml` and `pg_service.conf` from the team and place them in the meta directory:

```
Django-Hearthlight/
├── docker-compose.yaml
├── pg_service.conf
└── Hearthlight/        ← this repo
```

### 3. Start the database

From the meta directory (`Django-Hearthlight/`):

```bash
docker-compose up -d
```

### 4. Set up the project

```bash
cd Hearthlight
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Django Admin (with Jazzmin)

The Django admin is available at `http://localhost:8000/admin/`

### Jazzmin

Jazzmin is a Django app that provides a better admin experience.

## CMS Admin (Wagtail)

The CMS admin is available at `http://localhost:8000/cms-admin/`

### Wagtail

Wagtail is a CMS framework for Django.

You can read more about Wagtail development [here](https://docs.wagtail.org/en/stable/). Or about being an editor on a project using Wagtail [here](https://guide.wagtail.org/en-latest/).

## Django Management Commands

You can access the Django management commands with `python manage.py <command>`

### Management Commands

#### Create a new superuser

`python manage.py createsuperuser`

#### Run the server

`python manage.py runserver`

or with specific port number

`python manage.py runserver 8000` or `python manage.py runserver 0.0.0.0:8000`

## Django Shell

You can access the Django shell with `python manage.py shell`

### Shell Commands 

#### Create a new user

`from django.contrib.auth.models import User; User.objects.create_user('username', 'email@example.com', 'password')`

#### Create a new superuser

`from django.contrib.auth.models import User; User.objects.create_superuser('username', 'email@example.com', 'password')`

## Django Migrations

> [!Important]
> Do not commit development migrations to the repository. Wait until a branch is ready to be merged before committing migrations.

Create migrations after changing models:
- For a specific app: `python manage.py makemigrations <app_name>`
- For all apps: `python manage.py makemigrations`

Apply pending migrations: `python manage.py migrate`
