import os
import django
from django.apps import apps

# Setup Django environment (adjust `my_project.settings` to your project settings module)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject13.settings')
django.setup()

# Define the base directory for the templates
BASE_TEMPLATE_DIR = os.path.join('myapp13', 'templates', 'myapp13')
os.makedirs(BASE_TEMPLATE_DIR, exist_ok=True)

def generate_templates_for_model(model):
    """
    Generates CRUD templates for a given Django model, matching URL route names.
    """
    model_name = model._meta.object_name.lower()  # e.g., 'empleados'
    model_verbose_name = model._meta.verbose_name.title()  # e.g., 'Empleado'
    model_fields = model._meta.fields

    # Extract field names for displaying in the templates
    field_names = [field.name for field in model_fields if field.name != 'id']

    # List View Template
    list_template = f"""
{{% extends 'base.html' %}}
{{% block content %}}
<h1>{model_verbose_name} List</h1>
<a href="{{% url '{model_name}_create' %}}" class="btn btn-primary">Add New {model_verbose_name}</a>
<table class="table">
    <thead>
        <tr>
            {"".join([f"<th>{field.replace('_', ' ').title()}</th>" for field in field_names])}
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {{% for item in object_list %}}
        <tr>
            {"".join([f"<td>{{{{ item.{field} }}}}</td>" for field in field_names])}
            <td>
                <a href="{{% url '{model_name}_detail' item.pk %}}" class="btn btn-info btn-sm">View</a>
                <a href="{{% url '{model_name}_edit' item.pk %}}" class="btn btn-warning btn-sm">Edit</a>
                <a href="{{% url '{model_name}_delete' item.pk %}}" class="btn btn-danger btn-sm">Delete</a>
            </td>
        </tr>
        {{% endfor %}}
    </tbody>
</table>
{{% endblock %}}
"""

    # Detail View Template
    detail_template = f"""
{{% extends 'base.html' %}}
{{% block content %}}
<h1>{model_verbose_name} Details</h1>
{"".join([f"<p><strong>{field.replace('_', ' ').title()}:</strong> {{{{ object.{field} }}}}</p>" for field in field_names])}
<a href="{{% url '{model_name}_list' %}}" class="btn btn-secondary">Back to List</a>
<a href="{{% url '{model_name}_edit' object.pk %}}" class="btn btn-warning">Edit</a>
<a href="{{% url '{model_name}_delete' object.pk %}}" class="btn btn-danger">Delete</a>
{{% endblock %}}
"""

    # Form Template
    form_template = f"""
{{% extends 'base.html' %}}
{{% block content %}}
<h1>{{{{ 'Edit {model_verbose_name}' if object else 'Add New {model_verbose_name}' }}}}</h1>
<form method="post">
    {{% csrf_token %}}
    {{% for field in form.visible_fields %}}
    <div class="form-group">
        {{% field.label_tag %}}
        {{% field %}}
        {{% for error in field.errors %}}
        <p class="text-danger">{{{{ error }}}}</p>
        {{% endfor %}}
    </div>
    {{% endfor %}}
    <button type="submit" class="btn btn-success">Save</button>
    <a href="{{% url '{model_name}_list' %}}" class="btn btn-secondary">Cancel</a>
</form>
{{% endblock %}}
"""

    # Delete Confirmation Template
    delete_template = f"""
{{% extends 'base.html' %}}
{{% block content %}}
<h1>Delete {model_verbose_name}</h1>
<p>Are you sure you want to delete "{{{{ object }}}}"?</p>
<form method="post">
    {{% csrf_token %}}
    <button type="submit" class="btn btn-danger">Yes, delete</button>
    <a href="{{% url '{model_name}_list' %}}" class="btn btn-secondary">Cancel</a>
</form>
{{% endblock %}}
"""

    # Write templates to files
    templates = {
        f"{model_name}_list.html": list_template,
        f"{model_name}_detail.html": detail_template,
        f"{model_name}_form.html": form_template,
        f"{model_name}_confirm_delete.html": delete_template,
    }

    for template_name, content in templates.items():
        file_path = os.path.join(BASE_TEMPLATE_DIR, template_name)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Generated: {file_path}")


# Iterate over all models in the app and generate templates
app_name = 'myapp13'
app_config = apps.get_app_config(app_name)

for model in app_config.get_models():
    print(f"Generating templates for model: {model._meta.object_name}")
    generate_templates_for_model(model)

print("All templates have been generated successfully!")
