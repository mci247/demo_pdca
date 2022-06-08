# Generated by Django 4.0.5 on 2022-06-08 04:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pdca', '0002_alter_students_time_create'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('time_pub', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='students',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 11, 22, 2, 743988)),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=100)),
                ('vote', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdca.question')),
            ],
        ),
    ]
