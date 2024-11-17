import os
import django
from django.db import connection
from pathlib import Path
import psycopg2
# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject13.settings")
django.setup()

# Django imports
from django.apps import apps
from django.core.management import call_command

# Configurations
PROJECT_NAME = "myproject13"
APP_NAME = "myapp13"
DB_NAME = "DJANGOBUSMEN"
DB_USER = "videovig"
DB_PASSWORD = "$UA?uH3Y"
DB_HOST = "127.0.0.1"
DB_PORT = "5430"

BASE_DIR = Path(__file__).resolve().parent


def configure_settings():
    """Edit settings.py to configure the database and add the app to INSTALLED_APPS."""
    settings_path = BASE_DIR / PROJECT_NAME / "settings.py"
    print(f"Editing settings file: {settings_path}")

    if not settings_path.exists():
        print(f"Settings file not found at: {settings_path}")
        return

    with open(settings_path, "r") as file:
        lines = file.readlines()

    updated_lines = []
    inside_database_block = False
    installed_apps_updated = False
    c=0
    for line in lines:
        # Handle DATABASES block replacement
        if line.strip().startswith("DATABASES = {"):
            inside_database_block = True
            continue  # Skip the DATABASES start line
        if inside_database_block and line.strip() == "}":
            c+=1
            if c==2:
                inside_database_block = False
                c=0
            continue  # Skip the DATABASES end line
        if not inside_database_block:
            updated_lines.append(line)

        # Add new app to INSTALLED_APPS if not already added
        if "INSTALLED_APPS = [" in line and not installed_apps_updated:
            updated_lines.append(f"    '{APP_NAME}',\n")
            installed_apps_updated = True

    # Add the new DATABASES block
    new_database_block = f"""
DATABASES = {{
    'default': {{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{DB_NAME}',
        'USER': '{DB_USER}',
        'PASSWORD': '{DB_PASSWORD}',
        'HOST': '{DB_HOST}',
        'PORT': '{DB_PORT}',
    }}
}}
"""
    updated_lines.append(new_database_block)

    # Write the updated settings back to the file
    with open(settings_path, "w") as file:
        file.writelines(updated_lines)

    print("Settings file updated successfully.")





def get_tables_and_columns():
    """Query the database for tables and their columns."""
    connection = psycopg2.connect(
        dbname="DJANGOBUSMEN",
        user="videovig",
        password="$UA?uH3Y",
        host="127.0.0.1",
        port="5430"
    )
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """)
        tables = [row[0] for row in cursor.fetchall()]

        schema = {}
        for table in tables:
            cursor.execute(f"""
                SELECT column_name, data_type 
                FROM information_schema.columns 
                WHERE table_name = '{table}'
            """)
            columns = cursor.fetchall()
            schema[table] = columns

        return schema

def generate_models(schema):
    """Generate models dynamically based on the database schema."""
    models_path = BASE_DIR / APP_NAME / "models.py"
    with open(models_path, "w") as file:
        file.write("from django.db import models\n\n")
        for table, columns in schema.items():
            model_name = ''.join(word.title() for word in table.split('_'))
            file.write(f"class {model_name}(models.Model):\n")
            for column, data_type in columns:
                if column == "id":  # Skip the id field
                    continue
                # Determine the appropriate field type for the column
                field_type = "models.CharField(max_length=255)"  # Default field type
                if "int" in data_type:
                    field_type = "models.IntegerField()"
                elif "bool" in data_type:
                    field_type = "models.BooleanField()"
                elif "date" in data_type:
                    field_type = "models.DateField()"
                elif "timestamp" in data_type:
                    field_type = "models.DateTimeField()"

                # Write the field to the model
                file.write(f"    {column} = {field_type}\n")
            # Add the Meta class to configure the table mapping
            file.write(f"""
    class Meta:
        db_table = '{table}'
        managed = False
""")
            file.write("\n")


def create_views(schema):
    """Generate basic views for CRUD."""
    views_path = BASE_DIR / APP_NAME / "views.py"
    with open(views_path, "w") as file:
        file.write("from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView\n")
        file.write("from django.urls import reverse_lazy\n")
        file.write("from .models import *\n\n")
        for table in schema.keys():
            model_name = ''.join(word.title() for word in table.split('_'))
            file.write(f"""
class {model_name}ListView(ListView):
    model = {model_name}
    template_name = '{APP_NAME}/{table}_list.html'

class {model_name}DetailView(DetailView):
    model = {model_name}
    template_name = '{APP_NAME}/{table}_detail.html'

class {model_name}CreateView(CreateView):
    model = {model_name}
    fields = '__all__'
    template_name = '{APP_NAME}/{table}_form.html'
    success_url = reverse_lazy('{table}_list')

class {model_name}UpdateView(UpdateView):
    model = {model_name}
    fields = '__all__'
    template_name = '{APP_NAME}/{table}_form.html'
    success_url = reverse_lazy('{table}_list')

class {model_name}DeleteView(DeleteView):
    model = {model_name}
    template_name = '{APP_NAME}/{table}_confirm_delete.html'
    success_url = reverse_lazy('{table}_list')
""")


def create_urls(schema):
    """Generate URLs for CRUD."""
    urls_path = BASE_DIR / APP_NAME / "urls.py"
    with open(urls_path, "w") as file:
        file.write("from django.urls import path\n")
        file.write("from . import views\n\n")
        file.write("urlpatterns = [\n")
        for table in schema.keys():
            model_name = ''.join(word.title() for word in table.split('_'))
            file.write(f"    path('{table}/', views.{model_name}ListView.as_view(), name='{table}_list'),\n")
            file.write(f"    path('{table}/<int:pk>/', views.{model_name}DetailView.as_view(), name='{table}_detail'),\n")
            file.write(f"    path('{table}/create/', views.{model_name}CreateView.as_view(), name='{table}_create'),\n")
            file.write(f"    path('{table}/<int:pk>/edit/', views.{model_name}UpdateView.as_view(), name='{table}_edit'),\n")
            file.write(f"    path('{table}/<int:pk>/delete/', views.{model_name}DeleteView.as_view(), name='{table}_delete'),\n")
        file.write("]\n")


def create_templates(schema):
    """Generate basic templates for CRUD."""
    templates_dir = BASE_DIR / APP_NAME / "templates" / APP_NAME
    templates_dir.mkdir(parents=True, exist_ok=True)
    for table in schema.keys():
        with open(templates_dir / f"{table}_list.html", "w") as file:
            file.write(f"<h1>{table.title()} List</h1>\n")
            file.write("{% for obj in object_list %}\n")
            file.write("    <p>{{ obj }}</p>\n")
            file.write("{% endfor %}\n")


def include_app_urls_in_project():
    """Add the app's URLs to the project's main urls.py."""
    project_urls_path = BASE_DIR / PROJECT_NAME / "urls.py"
    print(f"Updating project URLs: {project_urls_path}")

    if not project_urls_path.exists():
        print(f"urls.py not found at: {project_urls_path}")
        return

    with open(project_urls_path, "r") as file:
        lines = file.readlines()

    updated_lines = []
    include_imported = False

    # Update or add the include import
    for line in lines:
        if line.strip() == "from django.urls import path":
            updated_lines.append("from django.urls import path, include\n")
            include_imported = True
        else:
            updated_lines.append(line)

    # Add the include import if it was missing entirely
    if not include_imported:
        updated_lines.insert(0, "from django.urls import include\n")

    # Check if the app's URLs are already included
    app_urls_included = any(f"path('{APP_NAME}/', include('{APP_NAME}.urls'))" in line for line in updated_lines)

    # Add the app URLs inclusion if not already added
    if not app_urls_included:
        for i, line in enumerate(updated_lines):
            if line.strip() == "urlpatterns = [":
                updated_lines.insert(i + 1, f"    path('{APP_NAME}/', include('{APP_NAME}.urls')),  # Include {APP_NAME} URLs\n")
                break

    # Write back to urls.py
    with open(project_urls_path, "w") as file:
        file.writelines(updated_lines)

    print(f"App URLs for {APP_NAME} added to {project_urls_path}.")




def main():
    """Main function to generate CRUD."""
    configure_settings()
    call_command("makemigrations")
    call_command("migrate")
    schema = get_tables_and_columns()
    generate_models(schema)
    create_views(schema)
    create_urls(schema)
    create_templates(schema)
    include_app_urls_in_project()  # Add the app URLs to the main project URLs
    call_command("makemigrations", APP_NAME)
    call_command("migrate")
    print("CRUD generated successfully!")


if __name__ == "__main__":
    main()
