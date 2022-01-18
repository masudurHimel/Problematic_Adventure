#!/bin/bash

echo "Installing Django"
pip install django

echo "Creating Django Project"
django-admin startproject project_name

cd project_name || exit

echo "Creating virtual venv"
virtualenv venv -p python3.8

echo "Activating venv"
source venv/bin/activate

echo "installing drf"
pip install django
pip install djangorestframework

pip list

echo "Migrating"
python manage.py migrate

echo "Running Project"
python manage.py runserver

#echo "Creating App"
#python manage.py startapp myapi
#add app_name in django settings (installed apps)




#For query : https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c
