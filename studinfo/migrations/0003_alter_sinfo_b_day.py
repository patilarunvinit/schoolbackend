# Generated by Django 4.2.1 on 2023-06-06 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studinfo', '0002_sinfo_delete_tt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinfo',
            name='b_day',
            field=models.DateField(max_length=8),
        ),
    ]
