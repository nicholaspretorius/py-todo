### Todo App

Todo App written in Python with Flask and SQLAlchemy as part of the Udacity Full Stack Web Developer Nanodegree course.

To run the app: 

* `python3 -m venv env` set the virtual environment for Pyhton // v3.7.4 for this example
* `source env/bin/activate` activate the venv
* `pip install -r requirements.txt` to install dependencies
* `export FLASK_ENV=development` to put app in debug mode [Optional]
* `python3 app.py` to run the app (http://127.0.0.1:5000/ or http://localhost:5000)
* Press Ctrl + C to quite the app
* `deactivate` de-activate the venv


#### Development

Steps taken during development: 

* `python3 -m venv env` set the virtual environment for Pyhton // v3.7.4 for this example
* `export FLASK_ENV=development` to put app in debug mode
* `export FLASK_ENV=` to exit debug mode (after Ctrl + C quits the app)
* `source env/bin/activate` activate the venv
* `pip install Flask` (note to self)
* `pip install flask-sqlalchemy`
* `pip install psycopg2`
* `pip install Flask-Migrate`
* `pip freeze > requirements.txt` writes the dependencies to file
* `deactivate` de-activate the venv when done developing
* /env folder is like 'node_modules'

#### Database

My local postgress setup is complicated, as such, I have Postgres running on port 5433.

* `dropdb todoapp -p 5433 && createdb todoapp -p 5433` (server must not be running to do this)
* `psql -p 5433`
* `\c todoapp` connects to the db
* `\dt` displays the tables in the db 
* `\d todos` displays the schema of the 'todos' table
* `INSERT INTO todos (description) VALUES ('Todo 1');`
* `SELECT * FROM todos`


#### Migrations

* `flask db init` setup migrations for the app

#### Linting

Developer in VS Code with flake8 linting. Code > Preferences > type in settings.json and click on 'Edit settings.json', add the [following](https://stackoverflow.com/a/50177174/4847180): 

`"python.linting.flake8Args": [
    "--max-line-length=120",
],`