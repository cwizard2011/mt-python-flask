[![CircleCI](https://circleci.com/gh/cwizard2011/mt-python-flask/tree/develop.svg?style=svg)](https://circleci.com/gh/cwizard2011/mt-python-flask/tree/develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/976733f46f2603b5804b/maintainability)](https://codeclimate.com/github/cwizard2011/mt-python-flask/maintainability)
## Maintenance Tracker
Maintenance Tracker App is an application that provides users with the ability to reach out to  operations or repairs department regarding repair or maintenance requests and monitor the  status of their request. 

# API FEATURE
Maintenance tracker has the following features:

# Authentication
- It makes use of jsonwebtoken for authentication
- Users have to supply their token after login to access all route

# Users
- It allows users to register by supplying details like: password, email, firstname and lastname
- Upon registration, a new user account will be created
- Registered users can access all the route except for admin routes

# Requests
- Authenticated users can create a request by supplying the title and details of the request
- Authenticated users can also get all requests that belong to them and not other users request
- Authenticated users can get a request by supplying the request Id and also see the current status of the request
- Authenticated users can edit a request for as long as the request status is still pending
- Authenticated users can delete a request for as long as the request status is still pending

# Admin
- Admin can view all users request
- Admin cannot create a request
- Admin can approve and disapprove any pending request
- Admin cannot resolve any approved request


## Development set up

- Check that python 3, pip, virtualenv and postgress are installed

- Check that python 3, pip, virtualenv and postgress are installed

- Clone the mt-api repo and cd into it
    ```
    git clone https://github.com/cwizard2011/mt-python-flask.git
    ```
- Create virtual env
    ```
    virtualenv --python=python3 venv
    ```
- Activate virtual env
    ```
    source venv/bin/activate
    ```
- Install dependencies
    ```
    pip install -r requirements.txt
    ```
- Create Application environment variables and save them in `.env` file or follow the example in `.env.example`
    ```
    export APP_SETTINGS="development"
    export SECRET_KEY=key
    export JWT_SECRET=jwt
    export JWT_EXPIRY="24hr"
    export JWT_PASSWORD_RESET_EXPIRY="1hr"
    export DATABASE_URL_DEV=development database url
    export DATABASE_URL_TEST= test database url
    export DATABASE_URL_PROD= production database url
    ```
- Running migrations

    - Initial migration commands
        ```
        $ alembic revision --autogenerate -m "Migration message"

        $ alembic upgrade head
        ```
    - If you have one migration file in the alembic/version folder. Run the commands below:
        ```
        $ alembic stamp head

        $ alembic upgrade head
        ```
    - If you have more than 2 migration files in the alembic/versions folder. Run the commands below
        ```
        $ alembic stamp head

        $ alembic upgrade head

        $ alembic revision --autogenerate -m "Your Migration message"
        
        $ alembic upgrade head
        
        ```
    
- Run application.
    ```
    python manage.py runserver
    ```
 Run all mutation through the endpoint `127.0.0.1:PORT/mt

- Running Tests
 - To run tests and observe test coverage for various versions of python . Run the command below.
 ```
 tox
 ```
 - To run  and check for test coverage. Run the command below:
 ```
 coverage run -m pytest
 ```
 - To obtain coverage report. Run the command below:

 ```
 coverage report
 ```
 - To obtain html browser report. Run command below:
 ```
 coverage html
 ```
 ```
 A folder titled html_coverage_report will be generated. Open it and copy the path  of index.html and paste it in your browser.
 ```

## Built with
- Python version  3
- Flask
- Grapghql
- Postgres

## Contribution guide
##### Contributing
There are lots of other features that can be added to this application like, few of which are:
- Super admin should be able to create other admin
- Super admin should be able to remove and block admin
- Admin and super admin should be able to delete a user
- User should be able to upload images
- User should be able to update their profile
- User should be able to update their password and also request for password reset when they forget password
- User should receive welcome email when they register to the application and also receive email notification when an admin approve, resolve or reject their request.

Other features can also be added using the contributor's initiatives.

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owner of this repository before making a change.

##### Pull Request Guide
- A contributor shall identify a feature, bug or chore to work on and reach out to the author of this project.
- The Contributor shall then create a branch off  the ` develop` branch where they are expected to undertake the task they have chosen.
- After  undertaking the task, a fully detailed pull request shall be submitted to the owners of this repository for review.
- If there any changes requested ,it is expected that these changes shall be effected and the pull request resubmitted for review.Once all the changes are accepted, the pull request shall be closed and the changes merged into `develop` by the owner of this repository.


# Author
Adeoye Peter