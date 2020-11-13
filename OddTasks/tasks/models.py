from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location = '/taskphotos/')

#source of information about the data in the database
#each model maps to a single database table
#fields are the only required part of a model
#field type helps Django decided how to populate database, how to render HTML

class Person(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    TASKS = [
        ('ML', 'Mow Lawn'),
        ('G', 'Groceries'),
        ('CH', 'Clean House'),
        ('SH', 'Snow Shoveling'),
        ('PH', 'Paint House'),
        ('RL', 'Rake Leaves'),
        ('M', 'Moving'),
        ('P', 'Plumbing')
    ]
    Task = models.CharField(max_length=2, choices=TASKS)
    Price = models.IntegerField()
    Phone = models.CharField(max_length=50)
    Location = models.CharField(max_length=120)

    def __str__(self):
        return self.Name

class Tasks(models.Model):
    TASKS = [
        ('ML', 'Mow Lawn'),
        ('G', 'Groceries'),
        ('CH', 'Clean House'),
        ('SH', 'Snow Shoveling'),
        ('M', 'Moving'),
        ('P', 'Plumbing')
    ]
    Task = models.CharField(max_length=30, choices= TASKS)
    Photo = models.FileField(storage = fs)
    Link = models.CharField(max_length = 50)

    def __str__(self):
        return self.Task