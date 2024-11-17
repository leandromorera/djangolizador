@echo off
:: Check if the project name is provided as a parameter
if "%1"=="" (
    echo Usage: create_django_project_with_param.bat [project_name]
    echo Example: create_django_project_with_param.bat myproject
    pause
    exit /b 1
)

:: Set project and app names
set PROJECT_NAME=%1
set APP_NAME=%2

:: Create the Django project
echo Creating Django project named %PROJECT_NAME%...
python -m django startproject %PROJECT_NAME%

:: Navigate into the project directory
cd %PROJECT_NAME% || (
    echo Failed to navigate to the project directory. Ensure the project was created successfully.
    pause
    exit /b 1
)

:: Create the Django app
echo Creating Django app named %APP_NAME%...
python manage.py startapp %APP_NAME%

:: Create additional directories and files
echo Setting up additional directories and files...

:: Templates directory
mkdir %APP_NAME%\templates\%APP_NAME%
echo ^{% ^extends "base.html" ^%} > %APP_NAME%\templates\%APP_NAME%\list.html
echo ^{% ^extends "base.html" ^%} > %APP_NAME%\templates\%APP_NAME%\detail.html
echo ^{% ^extends "base.html" ^%} > %APP_NAME%\templates\%APP_NAME%\form.html
echo ^{% ^extends "base.html" ^%} > %APP_NAME%\templates\%APP_NAME%\confirm_delete.html
echo <!DOCTYPE html^> > %APP_NAME%\templates\base.html
echo ^<html^>^<head^>^<title^>Dynamic CRUD^</title^>^</head^>^<body^>{% ^block content ^%}{% ^endblock ^%}^</body^>^</html^> >> %APP_NAME%\templates\base.html

:: Utils directory
mkdir %APP_NAME%\utils
echo from django.db import connection > %APP_NAME%\utils\db_inspector.py
echo def get_tables_and_relations(): pass >> %APP_NAME%\utils\db_inspector.py

:: Management commands directory
mkdir %APP_NAME%\management\commands
echo. > %APP_NAME%\management\__init__.py
echo. > %APP_NAME%\management\commands\__init__.py
echo import os > %APP_NAME%\management\commands\generate_models.py
echo def handle(*args, **kwargs): pass >> %APP_NAME%\management\commands\generate_models.py

:: Add URLs file
echo from django.urls import path > %APP_NAME%\urls.py
echo urlpatterns = [] >> %APP_NAME%\urls.py

:: Inform the user
echo Django project structure for %PROJECT_NAME% created successfully!
pause
