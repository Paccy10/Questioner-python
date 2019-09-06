# Questioner-python

[![Build Status](https://travis-ci.org/Paccy10/Questioner-python.svg?branch=develop)](https://travis-ci.org/Paccy10/Questioner-python) [![Maintainability](https://api.codeclimate.com/v1/badges/a5dce53b035062bd5f9f/maintainability)](https://codeclimate.com/github/Paccy10/Questioner-python/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/a5dce53b035062bd5f9f/test_coverage)](https://codeclimate.com/github/Paccy10/Questioner-python/test_coverage)

# Description

Crowd-source questions for a meetup. ​Questioner​​ helps the meetup organizer prioritize questions to be answered. Other users can vote on asked questions and they bubble to the top or bottom of the log.

# Installation and Setup

- Clone the repository

```
git clone https://github.com/Paccy10/Questioner-python.git
```

- Create a virtual environment
```
pipenv shell
```

- Install dependencies
```
pipenv install
```

- Make a copy of the .env.sample file and rename it to .env and update the variables accordingly:
```
DATABASE_URI = postgresql://YOUR_DATABASE_USER:YOUR_DATABASE_PASSWORD@YOUR_DATABASE_HOST/YOUR_DATABASE_NAME

TEST_DATABASE_URI = postgresql://YOUR_DATABASE_USER:YOUR_DATABASE_PASSWORD@YOUR_DATABASE_HOST/YOUR_TEST_DATABASE_NAME

SECRET_KEY=YOUR_SECRET_KEY
```

- Apply migrations
```
python manage.py db upgrade
```

- Should you make changes to the database models, run migrations as follows

    - Migrate database
    
    ```
    python manage.py db migrate
    ```

    - Upgrade to the new structure

    ```
    python manage.py db upgrade
    ```

- Run the application
```
python app.py
```    

# Running tests and generating report
```
pytest
```
To further view the lines not tested or covered if there is any, an `htmlcov` directory will be created, get the `index.html` file by entering the directory and view it in your browser.

# Documentation
- [Swagger](https://questioner-python.herokuapp.com/api/v1/documentation)


