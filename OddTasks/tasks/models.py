from django.db import models
from django.utils import timezone
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
    ]
    Task = models.CharField(max_length=2, choices=TASKS)
    Address = models.CharField(max_length=120)
    City = models.CharField(max_length=120)
    Province = models.CharField(max_length=2)
    Postal = models.CharField(max_length=7)
    Time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Name


class Client(Person):
    Money = models.DecimalField(max_digits=10, decimal_places=2)
    Description = models.CharField(max_length=1000)