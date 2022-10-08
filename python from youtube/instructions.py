'''
// install and chek version of python
pip install django
pip freeze

// create a dJango project
django-admin startproject projectName

// run the django project on port 7000
python manage.py runserver 7000

// create multiple app inside the django project
python manage.py startapp appName

// track the changes in apps. To do this you have to add the custom models in sitting.py file in INSTALLED_APPS array list
// create a migration class with directory for the model class
python manage.py makemigrations 

// pending customApp for database migration
// in one word, allow the custom created data models for database migration
python manage.py migrate

'''



