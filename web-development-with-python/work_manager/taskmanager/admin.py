from django.contrib import admin

from taskmanager.models import Project, Task, Supervisor, Developer

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Supervisor)
admin.site.register(Developer)
