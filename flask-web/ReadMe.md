# Flask Web application practice.

Simple web application built using flask.

Following project is structured/coded with my flavor on top of the tutorial materials.

tutorial source can be found official Flask web doc. http://flask.pocoo.org

## Setup

1. Install Python 3.7+
```bash
$ python --version
Python 3.7.0
```

2. Install virtualenv.
  - I recommend using `virtualenvwrapper`.
```bash
$ mkvirtualenv --python=$(which python3) flask-web && workon flask-web

(flask-web) $ ...
```

3. Install required dependencies.
```bash
$ pip install -r requirements.txt

...
```

## Execution

1. Use Makefile.
```bash
$ make run-dev

or

$ make run-prod
```

2. Visit/access `http://127.0.0.1:5000/hello` to check if api is running.
