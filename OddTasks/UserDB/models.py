from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Person(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField(MinValueValidator(1))
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)