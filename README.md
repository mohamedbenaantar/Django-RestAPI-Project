# Django-RestAPI-Project
Creating a Rest API Using DRF and Django

# 1. Install a VirtualEnvironment 
pip3 install pipenv

# 2. Create a new Environment 
pipenv shell

# this will create a Pipfile where all dependencies will be located

# 3. Install the Latest version of Django inside the 
pipenv install Django==4.2.5

# 4. to Check the packages installed inside the virtual environment 
pip3 freeze 

#[Useful Commands]
##  Create a Django Project
django-admin startproject IMDBApi

## Test the Django Running server
python3 manage.py runserver

# To change something inside settings goes to application folder which is the same name as a project folder

# Pipfile and Pipfile.lock is ignored in case anyone want to setUp the environement by himself

 cd IMDBApi  # inside the project folder not inside the app folder

 # create new app watchlist_app at the same level with manage.py
 python3 manage.py startapp watchlist_app

# create new app user_app
 python3 manage.py startapp user_app

# inside each app folder "watchlist_app and user_app" create a folder named api that will contain the views and urls, serializers, permissions files

cd watchlist_app
mkdir api

# install Django Rest Framework on the virtual environement
pipenv install djangorestframework