import os
import argparse

import data


def create_directories(app_name: str) -> None:
    """Create the project directories."""
    project_directory = f'{os.getcwd()}/{app_name}'
    os.makedirs(f'{project_directory}/src/templates')
    os.mkdir(f'{project_directory}/src/static')
    os.mkdir(f'{project_directory}/tests')


def create_readme(app_name: str) -> None:
    """Create a README.md file."""
    readme = open(f'{app_name}/README.md', 'w')
    readme.write(f'# {app_name}')
    readme.close()


def create_gitignore(app_name: str) -> None:
    """Create a .gitignore file."""
    gitignore = open(f'{app_name}/.gitignore', 'w')
    gitignore.write(data.GITIGNORE)
    gitignore.close()


def create_init(app_name: str) -> None:
    """Create an __init__.py file."""
    init = open(f'{app_name}/src/__init__.py', 'w')
    init.close()


def create_app(app_name: str) -> None:
    """Create an app.py file."""
    app = open(f'{app_name}/src/app.py', 'w')
    app.write(data.APP)
    app.close()


def create_base(app_name: str) -> None:
    """Create a base.html file."""
    base = open(f'{app_name}/src/templates/base.html', 'w')
    base.write(data.BASE)
    base.close()


def create_index(app_name: str) -> None:
    """Create an index.html file."""
    index = open(f'{app_name}/src/templates/index.html', 'w')
    index.write(data.INDEX)
    index.close()


def create_style(app_name: str) -> None:
    """Create a style.css file."""
    style = open(f'{app_name}/src/static/style.css', 'w')
    style.write(data.STYLE)
    style.close()


def create_conftest(app_name: str) -> None:
    """Create a conftest.py file."""
    conftest = open(f'{app_name}/tests/conftest.py', 'w')
    conftest.write(data.CONFTEST)
    conftest.close()


def create_test_app(app_name: str) -> None:
    """Create a test_app.py file."""
    test_app = open(f'{app_name}/tests/test_app.py', 'w')
    test_app.write(data.TEST_APP)
    test_app.close()


def create_files(app_name: str) -> None:
    """Create the project files."""
    create_readme(app_name)
    create_gitignore(app_name)
    create_init(app_name)
    create_app(app_name)
    create_base(app_name)
    create_index(app_name)
    create_style(app_name)
    create_conftest(app_name)
    create_test_app(app_name)


def create_flask_app(app_name: str) -> None:
    """Create a Flask application."""
    create_directories(app_name)
    create_files(app_name)
    print(f'Success! Created {app_name} at {os.getcwd()}/{app_name}')


def main() -> None:
    parser = argparse.ArgumentParser(description='Set up a Flask app by running one command.')
    parser.add_argument('app_name', type=str, help='name of flask application')
    args = parser.parse_args()
    create_flask_app(args.app_name)
