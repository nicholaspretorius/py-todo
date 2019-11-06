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
* `pip freeze > requirements.txt` writes the dependencies to file
* `deactivate` de-activate the venv when done developing
* /env folder is like 'node_modules'