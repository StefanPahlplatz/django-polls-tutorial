from django.shortcuts import render
from taskmanager.models import Project

# Create your views here.
class Index:
    @staticmethod
    def page(request):
        all_projects = Project.objects.all()
        return render(request, 'en/public/index.html', {'action': 'Display all projects', 'all_projects': all_projects})


class Connection:
    @staticmethod
    def page(request):
        my_var = "Hello World !"
        years = 15
        array = ["Paris", "London", "Washington"]
        return render(request, 'en/public/connection.html', {"my_var": my_var, "years": years, "array_city": array})
