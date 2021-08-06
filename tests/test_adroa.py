import sys
import os
import shutil

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../adroa')))
import adroa


def test_create_directories(directories) -> None:
    assert os.path.isdir('my-app/src/static')
    assert os.path.isdir('my-app/src/templates')
    assert os.path.isdir('my-app/tests')


def test_create_readme(directories) -> None:
    adroa.create_readme('my-app')
    readme = open('my-app/README.md', 'r')
    first_line = readme.readline()
    assert first_line == f'# my-app'


def test_create_gitignore(directories) -> None:
    adroa.create_gitignore('my-app')
    gitignore = open('my-app/.gitignore', 'r')
    first_line = gitignore.readline()
    assert first_line == 'venv/\n'


def test_create_init(directories) -> None:
    adroa.create_init('my-app')
    assert os.path.exists('my-app/src/__init__.py')


def test_create_app(directories) -> None:
    adroa.create_app('my-app')
    app = open('my-app/src/app.py', 'r')
    first_line = app.readline()
    assert first_line == 'from flask import Flask, render_template\n'


def test_create_base(directories) -> None:
    adroa.create_base('my-app')
    base = open('my-app/src/templates/base.html', 'r')
    first_line = base.readline()
    assert first_line == '<!DOCTYPE html>\n'


def test_create_index(directories) -> None:
    adroa.create_index('my-app')
    index = open('my-app/src/templates/index.html', 'r')
    first_line = index.readline()
    assert first_line == '{% extends "base.html" %}\n'


def test_create_style(directories) -> None:
    adroa.create_style('my-app')
    style = open('my-app/src/static/style.css', 'r')
    first_line = style.readline()
    assert first_line == 'body {\n'


def test_create_conftest(directories) -> None:
    adroa.create_conftest('my-app')
    conftest = open('my-app/tests/conftest.py', 'r')
    first_line = conftest.readline()
    assert first_line == 'import sys\n'


def test_create_test_app(directories) -> None:
    adroa.create_test_app('my-app')
    test_app = open('my-app/tests/test_app.py', 'r')
    first_line = test_app.readline()
    assert first_line == 'def test_routing(client):\n'


def test_create_files(directories) -> None:
    adroa.create_files('my-app')
    assert os.path.exists('my-app/README.md')
    assert os.path.exists('my-app/.gitignore')
    assert os.path.exists('my-app/src/__init__.py')
    assert os.path.exists('my-app/src/app.py')
    assert os.path.exists('my-app/src/templates/base.html')
    assert os.path.exists('my-app/src/templates/index.html')
    assert os.path.exists('my-app/src/static/style.css')
    assert os.path.exists('my-app/tests/conftest.py')
    assert os.path.exists('my-app/tests/test_app.py')


def test_create_flask_app() -> None:
    adroa.create_flask_app('my-app')
    assert os.path.isdir('my-app/src/static')
    assert os.path.isdir('my-app/src/templates')
    assert os.path.isdir('my-app/tests')
    assert os.path.exists('my-app/README.md')
    assert os.path.exists('my-app/.gitignore')
    assert os.path.exists('my-app/src/__init__.py')
    assert os.path.exists('my-app/src/app.py')
    assert os.path.exists('my-app/src/templates/base.html')
    assert os.path.exists('my-app/src/templates/index.html')
    assert os.path.exists('my-app/src/static/style.css')
    assert os.path.exists('my-app/tests/conftest.py')
    assert os.path.exists('my-app/tests/test_app.py')
    shutil.rmtree('my-app')
