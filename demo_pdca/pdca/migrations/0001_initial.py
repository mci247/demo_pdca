# Generated by Django 4.0.5 on 2022-06-07 23:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('time_create', models.DateTimeField(default=datetime.datetime(2022, 6, 8, 6, 19, 50, 565913))),
            ],
        ),
    ]