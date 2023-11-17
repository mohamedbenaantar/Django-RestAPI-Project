## Creating a Rest API Using DRF and Django

### 1. Clone the project first and install all required packages using the below commands

```sh
pip3 install pipenv  ## Install virtual envr
pipenv install ## this is will install all packages from Pipefile
```

### 2. you can list all virtual envr within your system using

```sh
pipenv --venv
## Switch to your desired virtual env
pipenv shell --activate <virtualenv-name>
```

### 3. To Install a package within your virtual env 

```sh
pipenv install Django==4.2.5
```

### 4. to List all packages within your virtual environment
pip3 freeze 

### [Useful Commands]

```sh
##  Create a Django Project
django-admin startproject IMDBApi

## Test the Django Running server
python3 manage.py runserver

## To change something inside settings goes to application folder which is the same name as a project folder

## Pipfile and Pipfile.lock is ignored in case anyone want to setUp the environement by himself

 cd IMDBApi  # inside the project folder not inside the app folder

 ## create new app watchlist_app at the same level with manage.py
 python3 manage.py startapp watchlist_app

## create new app user_app
 python3 manage.py startapp user_app

## inside each app folder "watchlist_app and user_app" create a folder named api that will contain the views and urls, serializers, permissions files

cd watchlist_app
mkdir api

## install Django Rest Framework on the virtual environement
pipenv install djangorestframework