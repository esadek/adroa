GITIGNORE = """venv/

*.pyc
__pycache__/

instance/

.pytest_cache/
.coverage
htmlcov/

dist/
build/
*.egg-info/"""

APP = """from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)"""

BASE = """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="{{ url_for('static', filename='style.css') }}" rel="stylesheet">
    <title>Flask App</title>
  </head>
  <body>
    {% block content %}{% endblock %}
  </body>
</html>"""

INDEX = """{% extends "base.html" %}

{% block content %}
  <h1>Flask App</h1>
  <p>Edit src/app.py, save, and reload.</p>
  <a href="https://flask.palletsprojects.com/" target="_blank">Learn Flask</a>
{% endblock %}"""

STYLE = """body {
  color: #AAAAAA;
  background-color: #111111;
  text-align: center;
}

h1, a {
  color: #FFFFFF;
}"""

CONFTEST = """import sys
import os

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from app import app

@pytest.fixture
def client():
    client = app.test_client()
    yield client"""

TEST_APP = """def test_routing(client):
    response = client.get('/')
    assert response.status_code == 200"""
