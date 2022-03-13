![SuperbAPI](logo.png)

*Welcome to SuperbAPI*, 
a super simple API implemented using Django and GraphQL.

- [Installation](#installation)
    - [1. Create virtual python environment](#1-create-virtual-python-environment)
    - [2. Activate virtual environment](#2-activate-virtual-environment)
    - [3. Installing dependencies](#3-installing-dependencies)
    - [4. Populating Database](#4-populating-database)
- [Running the API](#running-the-api)
- [Testing](#testing)
- [Contact](#contact)

# Installation

This project was built using:

Package | Version
:-- | :--
Python | 3.10.0
Django | 4.0.3
Graphene-Django | 3.0.0b7*

*this is a year-old beta release of graphene-django, their latest production build breaks with Django v4. Hopefully this is fixed in further releases. For more info see [here](https://github.com/graphql-python/graphene-django/issues/1284).

If you're on a *nix system, you can use `build.sh` (you may need to assign execute permissions) to fast-track the following installation steps. Read on if you **LOVE** manual installations!

First, we need to be  in the root directory of this repository after cloning. i.e.

    $ cd superbAPI

### 1. Create virtual python environment
    /* in superbAPI root directory */
    $ python -m venv <environment_name>

**TIP:** If you're making changes to the repo, it's handy to add your `<environment_name>` directory to the .gitignore file so that it isn't included when committing to git. The current .gitignore file has `env` listed, which is what I call my virtual environments. 

### 2. Activate virtual environment
    $ source <environment_name>/bin/activate    # linux/macOS
    $ ./<environment_name>/Scripts/activate     # windows
### 3. Installing dependencies
    $ pip install -r requirements.txt
### 4. Populating Database
We use fixtures to populate dummy data into a basic sqlite3 database. Django provides an easy API to load data into their database [here](https://docs.djangoproject.com/en/4.0/ref/django-admin/#loaddata). Before we do this though, we have to ensure the correct tables are created in the database.

    1. $ python manage.py makemigrations

    2. $ python manage.py migrate

    3. $ python manage.py loaddata users

You're ready to go!

# Running the API

The easiest way to run the API for fun is to use Django's built in development server and the Graphene UI.

**NOTE:** This API is not meant to be used in a production environment.

To run the development server:

    $ python manage.py runserver

And to use the Graphene UI for curating GraphQL queries, navigate to [http://localhost:8000/graphql](http://localhost:8000/graphql).

Have fun!

# Testing

To run the suite of tests for the API simply run the following:

    $ python manage.py test app

# Contact

If you have any questions or contributions please reach out to me at:

`tlscelsi@gmail.com`