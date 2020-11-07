# Generated by Django 3.1.3 on 2020-11-07 21:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Age', models.IntegerField(verbose_name=django.core.validators.MinValueValidator(1))),
                ('Username', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('Task', models.CharField(choices=[('ML', 'Mow Lawn'), ('G', 'Groceries'), ('CH', 'Clean House'), ('SH', 'Snow Shoveling'), ('PH', 'Paint House'), ('RL', 'Rake Leaves')], max_length=2)),
                ('Address', models.CharField(max_length=120)),
                ('City', models.CharField(max_length=120)),
                ('Province', models.CharField(max_length=2)),
                ('Postal', models.CharField(max_length=7)),
                ('Time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
