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
    with open(f'{app_name}/README.md', 'w') as readme:
        readme.write(f'# {app_name}')


def create_gitignore(app_name: str) -> None:
    """Create a .gitignore file."""
    with open(f'{app_name}/.gitignore', 'w') as gitignore:
        gitignore.write(data.GITIGNORE)


def create_init(app_name: str) -> None:
    """Create an __init__.py file."""
    os.mknod(f'{app_name}/src/__init__.py')


def create_app(app_name: str) -> None:
    """Create an app.py file."""
    with open(f'{app_name}/src/app.py', 'w') as app:
        app.write(data.APP)


def create_base(app_name: str) -> None:
    """Create a base.html file."""
    with open(f'{app_name}/src/templates/base.html', 'w') as base:
        base.write(data.BASE)


def create_index(app_name: str) -> None:
    """Create an index.html file."""
    with open(f'{app_name}/src/templates/index.html', 'w') as index:
        index.write(data.INDEX)


def create_style(app_name: str) -> None:
    """Create a style.css file."""
    with open(f'{app_name}/src/static/style.css', 'w') as style:
        style.write(data.STYLE)


def create_conftest(app_name: str) -> None:
    """Create a conftest.py file."""
    with open(f'{app_name}/tests/conftest.py', 'w') as conftest:
        conftest.write(data.CONFTEST)


def create_test_app(app_name: str) -> None:
    """Create a test_app.py file."""
    with open(f'{app_name}/tests/test_app.py', 'w') as test_app:
        test_app.write(data.TEST_APP)


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
