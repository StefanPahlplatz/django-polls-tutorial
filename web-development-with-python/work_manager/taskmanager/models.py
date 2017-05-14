from __future__ import unicode_literals

from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    login = models.CharField(max_length=25, verbose_name='Login')
    password = models.CharField(max_length=100, verbose_name='Password')
    phone = models.CharField(max_length=20, verbose_name='Phone number', null=True, default=None, blank=True)
    born_date = models.DateField(verbose_name='Born date', null=True, default=None, blank=True)
    last_connection = models.DateTimeField(verbose_name='Date of last connection', null=True, default=None, blank=True)
    email = models.EmailField(verbose_name='Email')
    years_seniority = models.IntegerField(verbose_name='Seniority', default=0)
    date_created = models.DateField(verbose_name='Date of birthday', auto_now_add=True)

    class Meta:
        abstract = True


class Supervisor(UserProfile):
    specialisation = models.CharField(max_length=50, verbose_name='Specialisation')

    def __str__(self):
        return self.name


class Developer(UserProfile):
    supervisor = models.ForeignKey(Supervisor, verbose_name='Supervisor', related_name='developer_supervisor')

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    description = models.CharField(max_length=1000, verbose_name='Description')
    client_name = models.CharField(max_length=1000, verbose_name='Client name')


class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    description = models.CharField(max_length=1000, verbose_name='Description')
    time_elapsed = models.IntegerField(verbose_name='Elapsed time', null=True, default=None, blank=True)
    importance = models.IntegerField(verbose_name='Importance')
    project = models.ForeignKey(Project, verbose_name='Project', null=True, default=None, blank=True, related_name='task_project')
    app_user = models.ForeignKey(Developer, verbose_name='User', related_name='task_user')
