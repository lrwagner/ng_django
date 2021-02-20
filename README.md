# dependencies
- node.js: https://nodejs.org/en/
    - install via `brew install node`
    - install via `conda install -c conda-forge nodejs`
- npm (included with node)
- angular: https://angular.io/
    - install via `npm install -g @angular/cli`
- python 3.9

# install
## 1. angular
install frontend
---
- cd into ./frontend
- run `npm install`

build app
---
- run `ng build`

## 2. python/django
go back to repo root dir

create venv
---
- `python -m venv .venv` or `conda create --prefix .venv python=3.9`

install requirements
---
- activate venv
- `pip install -r requirements/dev.txt`

django
---
- run `python manage.py makemigrations`
- run `python manage.py migrate`
- start with `python manage.py runserver`
