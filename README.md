wKRApp
=========

>wKRApp is the web front-end for the KRApp (Key Responsibility Area Application).

-----

## About

This web front-end will be the main user interface to the KRApp. The KRApp intends to automate and ease the workflows associated with Key Responsibility Area documents used for performance evaluations in many organisations. This KRApp will be developed in several phases:

- A Minimum Viable Prototype (MVP) will be created with just the front-end and mostly dummy data.
- The KRApp back-end or business logic will be created.
- The front-end will be continually refactored to use the working back-end functionality.

This web front-end is created in Python with the [Flask framework](http://flask.pocoo.org/).

## Contributing Guidelines

### Git Workflow

For non core team members please use the following workflow

```
Fork -> Feature/Issue Branch -> Pull Request -> Comment, Reiterate -> Merge 
```

### Commit Messages

Please follow [AngularJS Git Commit Message Conventions](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit).

### Python Style

Please ensure the python code adheres to [PEP 8](http://legacy.python.org/dev/peps/pep-0008/)

## Dependencies
_Optional:_ It is recommended that you use a python virtual environment for development: [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper)

You can install the python dependencies with pip:

```bash
pip install -r dependencies.txt
```

## Running on local server

Once you have the application and dependencies installed you can serve it locally.

```bash
# Previews the app on a local server
python runserver.py
```

## Documentation

No documentation for the MVP phase yet.
