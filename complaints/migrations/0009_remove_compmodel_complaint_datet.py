# Generated by Django 3.2.10 on 2024-01-18 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0008_alter_compmodel_complaint_datet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compmodel',
            name='complaint_dateT',
        ),
    ]
