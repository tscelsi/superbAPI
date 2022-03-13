# app

- [app](#app)
    - [models.py](#modelspy)
    - [schema.py](#schemapy)
    - [tests.py](#testspy)
    - [fixtures](#fixtures)

This directory contains the database models needed for the API to work as well as the GraphQL schema definitions.

### models.py

Contains the logic for the person and address sql tables.

### schema.py

Contains the logic for the GraphQL API endpoint defining how to return data to the client.

### tests.py

Contains unittests for superbAPI

### fixtures

This directory contains the fixtures used to initially populate the sqlite3 database with users (or in this case, a single user).