from django.contrib import admin
from Employee_App.models import Employee, CustomUser
from django.apps import apps

# Register your models here.
admin.site.register(Employee)
admin.site.register(CustomUser)

app = apps.get_app_config('graphql_auth')

for model_name, model in app.models.items():
    admin.site.register(model)
