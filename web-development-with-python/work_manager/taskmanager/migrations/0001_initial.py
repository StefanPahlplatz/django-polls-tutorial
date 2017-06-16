# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-14 09:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('login', models.CharField(max_length=25, verbose_name='Login')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
                ('phone', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Phone number')),
                ('born_date', models.DateField(blank=True, default=None, null=True, verbose_name='Born date')),
                ('last_connection', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Date of last connection')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('years_seniority', models.IntegerField(default=0, verbose_name='Seniority')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Date of birthday')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('client_name', models.CharField(max_length=1000, verbose_name='Client name')),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('login', models.CharField(max_length=25, verbose_name='Login')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
                ('phone', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Phone number')),
                ('born_date', models.DateField(blank=True, default=None, null=True, verbose_name='Born date')),
                ('last_connection', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Date of last connection')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('years_seniority', models.IntegerField(default=0, verbose_name='Seniority')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Date of birthday')),
                ('specialisation', models.CharField(max_length=50, verbose_name='Specialisation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('time_elapsed', models.IntegerField(blank=True, default=None, null=True, verbose_name='Elapsed time')),
                ('importance', models.IntegerField(verbose_name='Importance')),
                ('app_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_user', to='taskmanager.Developer', verbose_name='User')),
                ('project', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_project', to='taskmanager.Project', verbose_name='Project')),
            ],
        ),
        migrations.AddField(
            model_name='developer',
            name='supervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='developer_supervisor', to='taskmanager.Supervisor', verbose_name='Supervisor'),
        ),
    ]