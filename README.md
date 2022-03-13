![SuperbAPI](logo.png)

*Welcome to SuperbAPI*, 
a super simple API implemented using Django and GraphQL.



## Installation

This project was built using:

Package | Version
:-- | :--
Python | 3.10.0
Django | 4.0.3
Graphene-Django | 2.15.0

**NOTE:** A bug was encountered due to incompatibilities between Django v4.0 and the graphene_django packages. To fix, references to `force_text` in graphene_django/utils/utils.py source code must be changed to `force_str`. See: [this](https://github.com/graphql-python/graphene-django/issues/1284) link for more details and other solutions.


Navigate to the root directory of this repository after cloning.

### 1. Create virtual python environment
    /* in superbAPI root directory */
    $ python -m venv <environment_name>
### 2. Activate virtual environment
    $ source <environment_name>/bin/activate    # linux/macOS
    $ ./<environment_name>/Scripts/activate     # windows
### 3. Installing dependencies
    $ pip install -r requirements.txt
### 4. Populating Database
We use fixtures to populate dummy data into a basic sqlite3 database. Django provides an easy API to load data into their database [here](https://docs.djangoproject.com/en/4.0/ref/django-admin/#loaddata).

    $ python manage.py loaddata users

1. create virtual environment
2. install dependencies: pip install -r requirements.txt
3. update database with fixtures: python manage.py loaddata users
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py runserver