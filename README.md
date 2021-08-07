# Adroa

[![Build](https://img.shields.io/github/workflow/status/esadek/adroa/CI)](https://github.com/esadek/adroa/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/esadek/adroa)](https://github.com/esadek/adroa/blob/main/LICENSE)
[![Release](https://img.shields.io/github/v/release/esadek/adroa)](https://github.com/esadek/adroa/releases)

Set up a Flask app by running one command.

## Installation

Clone repository and change directory:

```
git clone https://github.com/esadek/adroa.git
cd adroa
```

## Usage

```
usage: adroa [-h] app_name

Set up a Flask app by running one command.

positional arguments:
  app_name    name of flask application

optional arguments:
  -h, --help  show this help message and exit
```

Run command, change directory, and run app:

```
python3 adroa my-app
cd my-app
python3 src/app.py
```

Then open [http://localhost:5000/](http://localhost:5000/) to see your app.

## Output

Running `python3 adroa my-app` will create a directory called `my-app` inside the current directory. Inside that directory, it will generate the initial project structure:

```
my-app/
├── README.md
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── templates/
│   │   ├── base.html
│   │   └── index.html
│   └── static/
│       └── style.css
└── tests/
    ├── conftest.py
    └── test_app.py
```

## License

Adroa is MIT licensed. See [LICENSE](https://github.com/esadek/adroa/blob/main/LICENSE) for details.