# Generated by Django 3.2.10 on 2024-01-18 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0006_auto_20240119_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compmodel',
            name='complaint_dateT',
            field=models.DateTimeField(null=True),
        ),
    ]
