from django.db import models
from django.contrib.auth.models import User


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
