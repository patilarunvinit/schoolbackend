# Generated by Django 3.2.10 on 2023-07-21 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='attandmod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=60, null=True)),
                ('name', models.CharField(max_length=60, null=True)),
                ('class_div', models.CharField(max_length=10, null=True)),
                ('roll_no1', models.CharField(max_length=5, null=True)),
                ('option', models.BooleanField(blank=True, default=False, null=True)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]