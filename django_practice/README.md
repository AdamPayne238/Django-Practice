
## ## THIS INFORMATION IS FROM THE DJANGO FUNDAMENTALS COURSE PLURALSIGHT ## ##

# MODELS, TEMPLATES, VIEWS make up a django

"""
When an HTTP request comes in
    Django looks in urls.py
        - urlpatterns variable
        - Holds a list of URL mappings
    URL mapping
        - Match URLs with regular expressions
        - Map URLs to views
"""
"""
Models
 - Python classes
 - Mapped to database tables
 - Each object is a row in the table
"""
"""
Migrations
    - Python Scripts
    - Keep DB structure in sync with code
    - Auto-generated (but not always)
"""
"""
Django Apps
    - Python package
    - Contain models, views, templates, urls
    - Most Django projects contain several apps (that make up the whole applicationk)
    - An example is a form app (for entire application)
"""

# /welcome the "r" string allows you to use backslashes
# and quotes inside the string ^ make sure it starts with
# welcome $ ends. both ^ and $ will only be welcome

You can start a new project in pycharm with Django and it will install django and virtual env

#A view is a django component that handles a request for a web page

Start server: python manage.py runserver
    - This will return a port that you can access the server in the browser

python manage.py startapp gameplay  # Gameplay is the name of app being created
(creates a gameplay app inside folder)
Also creates
    - __init__.py
    - admin.py
    - apps.py
    - migrations (initially empty)
    - models.py
    - tests.py
    - views.py
    
 Once you create an app you need
    - Add it to settings.py in INSTALLED_APPS = [ list ]
    - 'gameplay' # app we we created
    