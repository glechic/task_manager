from django.contrib import admin
from .models import Project, Task

for model in [Project, Task]:
    admin.site.register(model)
